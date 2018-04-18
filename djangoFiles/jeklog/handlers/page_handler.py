import copy

import os

from django.conf import settings

from base.handlers.yaml_handlers import YAMLHandler
from jeklog.handlers.scrape_files import FileScraper

from theJekyllProject.dbio import PageDbIO, RepoDbIO


class PageHandler(FileScraper):
    def __init__(self, user, repo_name):
        self.user = user
        self.repo_name = repo_name
        self.repo_path = '/'.join([settings.BASE_DIR, '..', 'JekLog',
                                   user.username, repo_name, ''])

    def handle_page_head(self, head_content):
        """
        Handle page head and create dict with different content
        """
        return_dict = {}
        return_dict['title'] = self.find_in_content(r'title:.+', head_content)
        return_dict['permalink'] = self.find_in_content(r'permalink:.+',
                                                        head_content)
        return return_dict

    def handle_page_body(self, body_content):
        """
        Handle page body and create page dict
        """
        return_dict = {}
        return_dict['content'] = self.markdown_to_html(body_content)
        return return_dict

    def page_call_scrapers(self, file_data):
        content = self.scrape_head_body(file_data)
        head_dict = self.handle_page_head(content['head'])
        body_dict = self.handle_page_body(content['body'])
        return self.join_dicts(head_dict, body_dict)

    def read_pages(self):
        """
        Read pages and save the instance into database
        """
        for file in os.listdir(self.repo_path):
            if file.endswith('.md'):
                if str(file) is not ('README.md' or '404.md'):
                    with open(self.repo_path + file, 'r') as page_file:
                        file_data = page_file.read()
                        content_dict = self.page_call_scrapers(file_data)
                        content_dict['repo'] = RepoDbIO().get_repo(
                            self.user, self.repo_name)
                        PageDbIO().save_db_instance(content_dict)


class AbstractPageHandler(PageHandler):
    """
    To use only the best of the earlier page handler
    """
    def __init__(self, repo_path):
        self.repo_path = repo_path

    def read_pages(self, repo, extension, exception_list):
        """
        read all files that we want at any time.
        we have to pass the extension and exception_list.
        exception_list will contain the list of all the files
        that should'nt be scanned.
        repo is the Repo db instance
        extension: 'markdown'
        exception_list: ('README', '404')
        """
        for file in os.listdir(self.path):
            if file.endswith('.'.join(['', extension])):
                if file not in exception_list:
                    content = self.read_file(file)
                    head_data, body_content = self.read_wrapped_content(
                        content, '---')
                    head_dict = YAMLHandler().read_yaml(head_data)
                    full_dict = copy.deepcopy(head_dict)
                    full_dict['content'] = body_content
                    full_dict['repo'] = repo
                    PageDbIO().save_db_instance(full_dict)
