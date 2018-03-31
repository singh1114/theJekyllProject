import os

from git import Repo

from base.handlers.path_handlers import PathHandler
from base.handlers.github_handler import GithubHandler
from base.handlers.yaml_handlers import YAMLHandler

from startbootstrap.dbio import SiteDataDbIO

from theJekyllProject.dbio import RepoDbIO


class SBSFormHandler:
    def __init__(self, user, repo):
        """
        :param user: logged in user
        :param repo: the main repo name
        """
        self.path = PathHandler(user, repo).create_repo_path()

    def load_site_initials(self, user, form_class):
        """
        Load the site data initials from the database
        """
        site_data = SiteDataDbIO().get_obj({
            'repo': RepoDbIO().get_repo(user)
        })
        if site_data is None:
            return form_class
        return form_class(initial=site_data.__dict__)

    def post_site_data(self, user, form_field_dict):
        """
        handle the post site data View method
        :param user: the logged in user
        :param form_field_dict: form field cleaned data
        :return:
        """
        RepoDbIO().get_repo(user)
        SiteDataDbIO().create_obj(**form_field_dict)
        config_path = os.path.join(self.path, '_config.yml')

        # Complete all the yaml operations
        yaml_dict = YAMLHandler().read_yaml_file(config_path, False)
        new_yaml = YAMLHandler().change_yaml(yaml_dict, form_field_dict)
        YAMLHandler().write_yaml(config_path, new_yaml)

        # Complete all the git operations
        repo = Repo(self.path)
        GithubHandler.commit_all_changes(repo, 'Change site data')
        GithubHandler.push_code(repo, 'gh-pages')
