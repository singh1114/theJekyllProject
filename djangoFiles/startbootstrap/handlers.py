from base.handlers.github_handler import GithubHandler

from startbootstrap.constants import StartBootstrap


class StartBootstrapHandler:
    def __init__(self, repo, user):
        self.repo = repo
        self.user = user
        self.gh_handler = GithubHandler(user, repo)

    def create_repo(self):
        auth_token = self.gh_handler.get_user_token()
        return self.gh_handler.create_remote_repo(auth_token)

    def clone_theme_repo(self, path):
        return self.gh_handler.clone_repo(StartBootstrap.FORKED_URL, path)
