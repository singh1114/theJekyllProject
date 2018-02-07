import os

import re


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

    def handle_post_head(self, head_content):
        """
        """
        # TODO work on this
        pass

    def handle_post_body(self, body):
        """
        """
        # TODO then this one
        pass

    def extract_post(self, file):
        """
        Extract the post into types of content.
        """
        with open(file, 'r') as post_file:
            file_data = post_file.read()

        regex_search = re.search('---([^-]+)---([^-]+)', file_data)
        self.handle_post_head(regex_search.group(1))
        self.handle_post_body(regex_search.group(2))

    def read_posts(self):
        """
        Read the _posts directory and iterate over all the files in the
        directory.
        """
        for file in os.listdir(self.posts_path):
            self.call_that_function(file)
