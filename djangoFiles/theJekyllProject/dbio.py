from base.dbio import BaseDbIO

from theJekyllProject.models import (
    Repo,
    SiteData
)


class RepoDbIO(BaseDbIO):
    """
    Database input output operations using this class
    """
    def __init__(self, model_name):
        self.model_name = Repo

    def create_repo_main_true(self, user, repo_name):
        self.model_name.objects.create(user=user, repo=repo_name, main=True)


class SiteDataDbIO(BaseDbIO):
    """
    Database I/O operations are handled using this class
    """
    def __init__(self, model_name):
        self.model_name = SiteData

    def create(self):
        pass
