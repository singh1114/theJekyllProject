from base.handlers.github_handler import GithubHandler
from base.handlers.path_handlers import PathHandler

from jeklog.handlers.page_handler import AbstractPageHandler

from startbootstrap.constants import StartBootstrap


class SBSHandler:
    def __init__(self, user, repo):
        self.repo = repo
        self.user = user
        self.gh_handler = GithubHandler(user, repo)
        self.path = PathHandler(user, repo).create_repo_path()

    def perform_initial_tasks(self):
        """
        Perform initial tasks. Tasks include:
            * get user token
            * create repo
            * clone repo to the particular location
            * change config of the git repo
            * commit all changes
            * push code to remote
        """
        user_token = self.gh_handler.get_user_token()
        self.gh_handler.create_remote_repo(user_token)
        repo_path = PathHandler(self.user, self.repo).create_repo_path
        repo = self.gh_handler.clone_repo(StartBootstrap.FORKED_URL, repo_path)
        self.gh_handler.change_config(repo)
        self.gh_handler.commit_all_changes(repo, 'Intial commit')
        self.gh_handler.push_code(repo)
        self.fill_page_database()

    def fill_page_database(self):
        """
        This method will be used to fill the page database by iterating
        over the pages in the database.
        """
        AbstractPageHandler(self.path).read_pages(self.repo, 'html', [])
