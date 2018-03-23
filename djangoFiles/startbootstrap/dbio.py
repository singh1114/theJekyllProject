from base.dbio import AbstractBaseDbIO

from theJekyllProject.models import SiteData


class SiteDataDbIO(AbstractBaseDbIO):
    """
    Database I/O operations are handled using this class
    """
    def __init__(self):
        self.model_name = SiteData
