import os

from base.handlers.github_handler import GithubHandler
from base.handlers.path_handlers import PathHandler
from base.handlers.yaml_handlers import YAMLHandler

from jeklog.handlers.page_handler import AbstractPageHandler

from jekyllnow.constants import JekyllNow

from theJekyllProject.choices import BlogTemplates
from theJekyllProject.dbio import RepoDbIO, SiteDataDbIO


class JekyllNowHandler:
    def __init__(self, user, repo):
        self.user = user
        self.repo = repo
        self.gh_handler = GithubHandler(user, repo)
        self.path = PathHandler(user, repo).create_repo_path()
        self.yaml_handler = YAMLHandler()

    def perform_initial_tasks(self):
        """
        Perform initial tasks. Tasks include:
            * get user token
            * create repo
            * clone repo to the particular location
            * change config of the git repo
            * commit all changes
            * push code to remote
        """
        user_token = self.gh_handler.get_user_token()
        self.gh_handler.create_remote_repo(user_token)
        repo = self.gh_handler.clone_repo(JekyllNow.FORKED_URL, self.path)
        self.gh_handler.change_config(repo)
        self.gh_handler.gh_pages_branch(repo)
        repo_obj = RepoDbIO().get_obj({
            'user': self.user,
            'main': True,
            'repo': self.repo
        })
        self.update_baseurl(repo_obj)
        self.gh_handler.commit_all_changes(repo, 'Intial commit')
        self.gh_handler.push_code(repo)
        self.fill_page_database(repo_obj)
        self.update_template_name(repo_obj)

    def update_baseurl(self, repo_obj):
        """
        update baseurl in config file.
        """
        config_path = os.path.join(self.path, '_config.yml')
        yaml_dict = self.yaml_handler.read_yaml_file(config_path, True)
        if repo_obj.repo != (str(self.user.username) + '.github.io'):
            new_yaml = self.yaml_handler.change_yaml(yaml_dict,
                {'baseurl': "/{}".format(str(repo_obj.repo))})
            self.yaml_handler.write_dict_yaml(config_path, new_yaml)

    def update_template_name(self, repo):
        """
        update the template name to jekyllnow
        """
        RepoDbIO().update_obj(repo, {'template': BlogTemplates.JEKYLL_NOW})

    def fill_page_database(self, repo):
        """
        This method will be used to fill the page database by iterating
        over the pages in the database.
        """
        AbstractPageHandler(self.path).read_pages(repo, 'md',
            ('README.md', '404.md'))

    def perform_site_data(self, data_dict):
        """
        Perform all the site data operations here.
        """
        repo = RepoDbIO().get_obj({
            'user': self.user,
            'main': True,
        })
        config_path = os.path.join(self.path, '_config.yml')
        site_data = SiteDataDbIO().get_obj({'repo': repo})
        if site_data:
            SiteDataDbIO().update_obj(site_data, data_dict)
        else:
            SiteDataDbIO().save_db_instance(data_dict)
        self.del_key(data_dict, 'repo')
        yaml_dict = self.yaml_handler.read_yaml_file(config_path, True)
        new_yaml = self.yaml_handler.change_yaml(yaml_dict, data_dict)
        self.yaml_handler.write_dict_yaml(config_path, new_yaml)
        repo = self.gh_handler.get_repo_from_path(self.path)
        self.gh_handler.commit_all_changes(repo, 'Intial commit')
        self.gh_handler.push_code(repo)


    def del_key(self, dict, key):
        del dict[key]
