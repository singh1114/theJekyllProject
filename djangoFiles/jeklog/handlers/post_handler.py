import os

from django.conf import settings

from jeklog.handlers.scrape_files import FileScraper
from theJekyllProject.dbio import PostDbIO, RepoDbIO


class PostHandler(FileScraper):
    """
    Post handler will used to do all the operations related to Posts
    """
    def __init__(self, user, repo_name):
        self.user = user
        self.repo_name = repo_name
        self.posts_path = '/'.join([settings.BASE_DIR, '..', 'JekLog',
                                   self.user.username, self.repo_name,
                                   '_posts', ''])

    def handle_post_head(self, head_content):
        """
        Read and parse the head/meta content of the blog
        """
        return_data = {}
        return_data['author'] = self.find_in_content(
            r'author:.+|author:', head_content)
        return_data['comments'] = self.find_in_content(
            r'comments:.+|comments:', head_content)
        return_data['date'] = self.find_in_content(r'date:.+|date:',
                                                   head_content)
        return_data['layout'] = self.find_in_content(r'layout:.+|layout:',
                                                     head_content)
        return_data['title'] = self.find_in_content(r'title:.+|title:',
                                                    head_content)
        return_data['slug'] = self.find_in_content(r'slug:.+|slug:',
                                                   head_content)
        # TODO take care of categories as well
        return return_data

    def handle_body(self, body_content):
        """
        Read and parse the body of the content
        """
        return_data = {}
        return_data['content'] = self.markdown_to_html(body_content)
        return return_data

    def extract_post(self, file):
        """
        Extract the post into types of content.
        """
        with open(file, 'r') as post_file:
            file_data = post_file.read()
        return file_data

    def call_scrapers(self, file_data, is_post=True):
        """
        call various scrapers and return the results
        """
        content = self.scrape_head_body(file_data)
        head_dict = self.handle_post_head(content['head'])
        body_dict = self.handle_body(content['body'])
        # TODO With python 3 use main_dict = {**head_dict, **body_dict}
        return self.join_dicts(head_dict, body_dict)

    def read_posts(self):
        """
        Read the _posts directory and iterate over all the files in the
        directory. In the end save the instance in the database.
        """
        for file in os.listdir(self.posts_path):
            file_data = self.extract_post(self.posts_path + file)
            content_dict = self.call_scrapers(file_data)
            if content_dict['comments'] == 'true':
                content_dict['comments'] = True
            else:
                content_dict['comments'] = False
            content_dict['repo'] = RepoDbIO().get_repo(self.user,
                                                       self.repo_name)
            PostDbIO().save_db_instance(content_dict)
