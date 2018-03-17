from git import Repo

from github import Github

from django.contrib.auth.models import User


class GithubHandler:
    def __init__(self, user, repo=None):
        self.user = user
        self.repo = repo

    def get_user_token(self):
        user = User.objects.get(username=self.user.username)
        social = user.social_auth.get(provider='github')
        return social.extra_data['access_token']

    def create_remote_repo(self, auth_token):
        github = Github(auth_token)
        user = github.get_user()
        return user.create_repo(self.repo)

    def clone_repo(self, url, path):
        return Repo.clone_from(url, path)

    def change_config(self, repo):
        try:
            config = repo.config_writer()
        except IOError:
            #FIXME delete the lock file
            pass
        config = repo.config_writer()
        url = ('https://' + str(self.user.username) + ':' +
               str(self.get_user_token()) + '@github.com/' +
               str(self.user.username) + '/' + repo + '.git')
        # FIXME check the output of the repo
        config.set_value('remote "origin"', 'url', url)
        return config

    def commit_all_changes(self, repo, message):
        return repo.git.commit('-am', message)

    def push_code(self, repo, branch='gh-pages'):
        return repo.remotes.origin.push(branch)
