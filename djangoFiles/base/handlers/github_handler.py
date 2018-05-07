from git import Repo
from git.exc import GitCommandError

from github import Github
from github import GithubException

from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

from base.constants import DIR_ALREADY_PRESENT


class GithubHandler:
    def __init__(self, user, repo=None):
        self.user = user
        self.repo = repo

    def get_user_token(self):
        """
        get the user token using this method
        """
        user = User.objects.get(username=self.user.username)
        social = user.social_auth.get(provider='github')
        return social.extra_data['access_token']

    def create_remote_repo(self, auth_token):
        """
        creates an empty repo in the remote
        auth_token: authentication token of the user
        """
        github = Github(auth_token)
        user = github.get_user()
        try:
            repo = user.create_repo(self.repo)
        except GithubException as e:
            raise PermissionDenied(
                (e._GithubException__data['message'] +
                 e._GithubException__data['errors'][0]['message']))

    def clone_repo(self, url, path):
        """
        clone repo using this method
        url: URL of the repo to be cloned
        path: path where the repo is to be cloned
        """
        try:
            return Repo.clone_from(url, path)
        except GitCommandError:
            raise PermissionDenied(DIR_ALREADY_PRESENT)

    def change_config(self, repo):
        """
        We have to change the config with the user auth_token so that the push
        doesn't ask for username and password.
        - repo: name of repo is required.
        """
        # TODO test this function
        with repo.config_writer() as config:
            url = ('https://' + str(self.user.username) + ':' +
                   str(self.get_user_token()) + '@github.com/' +
                   str(self.user.username) + '/' + self.repo + '.git')
            config.set_value('remote "origin"', 'url', url)
            return config

    @staticmethod
    def commit_all_changes(repo, message):
        """
        commit all changes using this method
        repo: the repo object.
        message: message to be written in the commit
        """
        try:
            return repo.git.commit('-am', message)
        except Exception as e:
            pass

    @staticmethod
    def gh_pages_branch(repo):
        """
        create gh-pages branch and checkout to it.
        """
        repo.git.branch('gh-pages')
        repo.git.checkout('gh-pages')

    @staticmethod
    def push_code(repo, branch='gh-pages'):
        """
        push the code using this method
        repo: the git.Repo object
        branch: the branch in which you want to push the code
        """
        return repo.remotes.origin.push(branch)

    def get_repo_from_path(self, path):
        return Repo(path)
