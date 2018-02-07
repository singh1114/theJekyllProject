from django.conf import settings


class PostHandler:
    """
    Post handler will used to do all the operations related to Posts
    """
    def __init__(self, user, repo_name):
        self.base_dir = settings.BASE_DIR
        self.posts_path = '/'.join([self.base_dir, '..', 'JekLog',
                                   self.user.username, self.repo_name,
                                   'posts'])

    def read_posts(self):
        """
        Read the _posts directory and iterate over all the files in the
        directory.
        """
        pass
