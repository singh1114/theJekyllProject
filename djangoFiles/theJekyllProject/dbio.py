from base.dbio import BaseDbIO

from theJekyllProject.models import (
    Page, Post, Repo, SiteData, SiteExclude, SiteSocialProfile, SitePlugin,
    SiteTheme
)


class RepoDbIO(BaseDbIO):
    """
    Database input output operations using this class
    """
    def __init__(self):
        self.model_name = Repo

    def create_return(self, kwargs):
        """
        This model has a special requirement to return the saved instance
        """
        return self.model_name.objects.create(**kwargs)

    def get_repo(self, user, repo_name):
        """
        get the repo by name, logged_in user and main True
        """
        return self.model_name.objects.get(main=True,
                                           user=user, repo=repo_name)

    def change_main(self, user, repo):
        """
        Change the main repo, set main false for all other repos
        """
        all_repos = Repo.objects.filter(user=user, main=True)
        current_repo = repo
        for repo in all_repos:
            if repo.id is not current_repo.id:
                repo.main = False
                repo.save()
        current_repo.main = True
        current_repo.save()

class SiteDataDbIO(BaseDbIO):
    """
    Database I/O operations are handled using this class
    """
    def __init__(self):
        self.model_name = SiteData


class SiteSocialProfileDbIO(BaseDbIO):
    """
    Database I/O operations are handled using this class
    """
    def __init__(self):
        self.model_name = SiteSocialProfile


class SiteThemeDbIO(BaseDbIO):
    """
    Database I/O operations are handled using this class
    """
    def __init__(self):
        self.model_name = SiteTheme


class SitePluginDbIO(BaseDbIO):
    """
    Database I/O operations are handled using this class
    """
    def __init__(self):
        self.model_name = SitePlugin


class SiteExcludeDbIO(BaseDbIO):
    """
    Database I/O operations are handled using this class
    """
    def __init__(self):
        self.model_name = SiteExclude


class PostDbIO(BaseDbIO):
    """
    Database I/O operations are handled using this class
    """
    def __init__(self):
        self.model_name = Post


class PageDbIO(BaseDbIO):
    """
    Database I/O operations are handled using this class
    """
    def __init__(self):
        self.model_name = Page
