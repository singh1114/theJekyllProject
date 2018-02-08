import os

import re

from markdown2 import Markdown

from django.conf import settings

from jeklog.handlers.scrape_files import FileScraper
from theJekyllProject.dbio import PostDbIO

class PostHandler:
    """
    Post handler will used to do all the operations related to Posts
    """
    def __init__(self, user, repo_name):
        self.fs = FileScraper()
        self.posts_path = '/'.join([settings.BASE_DIR, '..', 'JekLog',
                                   self.user.username, self.repo_name,
                                   'posts'])

    def markdown_to_html(self, content):
        """
        Convert the read markdown to html
        """
        return Markdown().convert(content)

    def handle_post_head(self, head_content):
        """
        Read and parse the head/meta content of the blog
        """
        return_data = {}
        return_data['author'] = self.fs.find_in_content(r'author:.+|author:',
                                                        head_content)
        return_data['comment'] = self.fs.find_in_content(r'comment:.+|comment:'
                                                         , head_content)
        return_data['date'] = self.fs.find_in_content(r'date:.+|date:',
                                                      head_content)
        return_data['layout'] = self.fs.find_in_content(r'layout:.+|layout:',
                                                        head_content)
        return_data['title'] = self.fs.find_in_content(r'title:.+|title:',
                                                       head_content)
        return_data['slug'] = self.fs.find_in_content(r'slug:.+|slug:',
                                                      head_content)
        # TODO take care of categories as well
        return return_data

    def handle_post_body(self, body):
        """
        Read and parse the body of the content
        """
        return_data = {}
        return_data['content'] = self.markdown_to_html(body)
        return return_data

    def extract_post(self, file):
        """
        Extract the post into types of content.
        """
        with open(file, 'r') as post_file:
            file_data = post_file.read()

        regex_search = re.search('---([^-]+)---([^-]+)', file_data)
        head_dict = self.handle_post_head(regex_search.group(1))
        body_dict = self.handle_post_body(regex_search.group(2))
        # With python 3 use main_dict = {**head_dict, **body_dict}
        main_dict = head_dict.copy()
        main_dict.update(body_dict)
        return main_dict

    def read_posts(self):
        """
        Read the _posts directory and iterate over all the files in the
        directory.
        """
        for file in os.listdir(self.posts_path):
            content_dict = self.call_that_function(file)
            PostDbIO.save_db_instance(content_dict)
