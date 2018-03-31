from base.dbio import AbstractBaseDbIO

from theJekyllProject.models import SiteData, SiteSocialProfile


class SiteDataDbIO(AbstractBaseDbIO):
    """
    Database I/O operations are handled using this class
    """
    def __init__(self):
        self.model_name = SiteData


class SocialProfileDbIO(AbstractBaseDbIO):
    """
    Database I/O operations are handled using this class
    """
    def __init__(self):
        self.model_name = SiteSocialProfile
