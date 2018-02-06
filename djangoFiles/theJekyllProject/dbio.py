from base.dbio import BaseDbIO

from theJekyllProject.models import (
    Repo, SiteData, SiteExclude, SiteSocialProfile, SitePlugin, SiteTheme
)


class RepoDbIO(BaseDbIO):
    """
    Database input output operations using this class
    """
    def __init__(self, model_name):
        self.model_name = Repo


class SiteDataDbIO(BaseDbIO):
    """
    Database I/O operations are handled using this class
    """
    def __init__(self, model_name):
        self.model_name = SiteData


class SiteSocialProfileDbIO(BaseDbIO):
    """
    Database I/O operations are handled using this class
    """
    def __init__(self, model_name):
        self.model_name = SiteSocialProfile


class SiteThemeDbIO(BaseDbIO):
    """
    Database I/O operations are handled using this class
    """
    def __init__(self, model_name):
        self.model_name = SiteTheme


class SitePluginDbIO(BaseDbIO):
    """
    Database I/O operations are handled using this class
    """
    def __init__(self, model_name):
        self.model_name = SitePlugin


class SiteExcludeDbIO(BaseDbIO):
    """
    Database I/O operations are handled using this class
    """
    def __init__(self, model_name):
        self.model_name = SiteExclude
