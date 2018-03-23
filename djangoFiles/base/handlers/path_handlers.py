from django.conf import settings


class PathHandler:
    def __init__(self, user, repo):
        self.user = user
        self.repo = repo

    @property
    def create_repo_path(self):
        return '/'.join([settings.BASE_DIR, '..', 'JekLog',
                         self.user.username, self.repo])
