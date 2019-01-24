from base.dbio import AbstractBaseDbIO

from logs.models import AccessLog


class AccessLogDbIO(AbstractBaseDbIO):

    def __init__(self):
        self.model_name = AccessLog
