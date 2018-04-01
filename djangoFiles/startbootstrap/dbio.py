from base.dbio import AbstractBaseDbIO

from theJekyllProject.models import Post, SiteData, SiteSocialProfile


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


class PostDbIO(AbstractBaseDbIO):
    """
    Database I/O operations are handled using this class
    """
    def __init__(self):
        self.model_name = Post
