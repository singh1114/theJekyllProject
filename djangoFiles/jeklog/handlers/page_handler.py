import os

from django.conf import settings

from jeklog.handlers.post_handler import PostHandler
from jeklog.handlers.scrape_files import FileScraper

from theJekyllProject.dbio import PageDbIO


class PageHandler(FileScraper):
    def __init__(self, user, repo):
        self.repo_path = '/'.join([settings.BASE_DIR, '..', 'JekLog',
                                   self.user.username, self.repo_name])

    def handle_page_head(self, head_content):
        """
        Handle post head and create dict with different content
        """
        return_dict = {}
        return_dict['title'] = self.find_in_content(r'title:.+', head_content)
        return_dict['permalink'] = self.find_in_content(r'permalink:.+',
                                                        head_content)
        return return_dict

    def handle_page_body(self, body_content):
        """
        Handle post body and create body dict
        """
        PostHandler().handle_body(body_content)


    def read_page(self):
        """
        Read pages and save the instance into database
        """
        for file in os.listdir(self.repo_path):
            if file.endswith('.md'):
                if str(file) is not ('README.md' or '404.md'):
                    with open(file, 'r') as page_file:
                        file_data = page_file.read()
            content_dict = PostHandler().call_scrapers(file_data)
            PageDbIO.save_db_instance(content_dict)
