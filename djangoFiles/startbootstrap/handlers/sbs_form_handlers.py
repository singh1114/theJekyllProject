import os

from git import Repo

from django.core.exceptions import PermissionDenied

from base.handlers.extra_handlers import ExtraHandler
from base.handlers.file_handler import FileHandler
from base.handlers.form_handler import FormHandler
from base.handlers.path_handlers import PathHandler
from base.handlers.github_handler import GithubHandler
from base.handlers.yaml_handlers import YAMLHandler

from startbootstrap.dbio import PostDbIO, SiteDataDbIO, SocialProfileDbIO

from theJekyllProject.dbio import RepoDbIO


class SBSFormHandler:
    def __init__(self, user, repo):
        """
        :param user: logged in user
        :param repo: the main repo name
        """
        self.path = PathHandler(user, repo).create_repo_path()

    def load_site_initials(self, request, form_class):
        """
        Load the site data initials from the database
        """
        site_data = SiteDataDbIO().get_obj({
            'repo': RepoDbIO().get_repo(request.user)
        })
        return FormHandler(request, form_class).load_initials(site_data)

    def post_site_data(self, user, form_field_dict):
        """
        handle the post site data View method
        :param user: the logged in user
        :param form_field_dict: form field cleaned data
        :return:
        """
        repo = RepoDbIO().get_repo(user)
        form_field_dict['repo'] = repo
        site_data = SiteDataDbIO().get_obj({'repo': repo})

        if site_data:
            SiteDataDbIO().update_obj(site_data, form_field_dict)
        else:
            SiteDataDbIO().create_obj(**form_field_dict)

        config_path = os.path.join(self.path, '_config.yml')

        self.del_repo(form_field_dict)
        # Complete all the yaml operations
        yaml_dict = YAMLHandler().read_yaml_file(config_path, True)
        new_yaml = YAMLHandler().change_yaml(yaml_dict, form_field_dict)
        YAMLHandler().write_dict_yaml(config_path, new_yaml)

        # Complete all the git operations
        repo = Repo(self.path)
        GithubHandler.commit_all_changes(repo, 'Change site data')
        GithubHandler.push_code(repo, 'gh-pages')

    def load_social_profile_initials(self, request, form_class):
        """
        Load the site profile initials from the database
        """
        social_data = SocialProfileDbIO().get_obj({
            'repo': RepoDbIO().get_repo(request.user)
        })
        return FormHandler(request, form_class).load_initials(social_data)

    def post_social_profile_data(self, user, form_field_dict):
        """
        handle the post social profile View method
        :param user: the logged in user
        :param form_field_dict: form field cleaned data
        :return:
        """
        repo = RepoDbIO().get_repo(user)

        # repo is the foriegn key so it needs to be in the dict.
        form_field_dict['repo'] = repo
        social_data = SocialProfileDbIO().get_obj({'repo': repo})

        if social_data:
            SocialProfileDbIO().update_obj(social_data, form_field_dict)
        else:
            SocialProfileDbIO().create_obj(**form_field_dict)

        config_path = os.path.join(self.path, '_config.yml')

        self.del_repo(form_field_dict)
        # Complete all the yaml operations
        yaml_dict = YAMLHandler().read_yaml_file(config_path, True)
        new_yaml = YAMLHandler().change_yaml(yaml_dict, form_field_dict)
        YAMLHandler().write_dict_yaml(config_path, new_yaml)

        # Complete all the git operations
        repo = Repo(self.path)
        GithubHandler.commit_all_changes(repo, 'Change site data')
        GithubHandler.push_code(repo, 'gh-pages')

    def load_posts_initials(self, request, form_class, pk=None):
        """
        Load the site profile initials from the database
        """
        repo = RepoDbIO().get_repo(request.user)
        if pk:
            post = PostDbIO().get_obj({
                'pk': pk,
                'repo__user': request.user,
                'repo': repo
            })
            if post is None:
                raise PermissionDenied
        else:
            post = None

        return FormHandler(request, form_class).load_initials(post)

    def post_posts_data(self, user, form_field_dict, pk=None):
        """
        handle the post posts View method
        :param user: the logged in user
        :param form_field_dict: form field cleaned data
        We have to delete the file if the title is changed otherwise two
        different files will be created.
        :return:
        """
        # TODO image copying is not done and delete the old one.
        repo = RepoDbIO().get_repo(user)
        if pk:
            post = PostDbIO().get_obj({
                'pk': pk,
                'repo__user': user,
                'repo': repo
            })
            if pk is None:
                raise PermissionDenied

            if post.title is not form_field_dict['title']:
                file_name = ExtraHandler().file_name_f_title(post.title,
                                                             'html')
                FileHandler('/'.join([self.path, '_posts']),
                            file_name).delete_file()

            post = PostDbIO().update_obj(post, **form_field_dict)

        else:
            form_field_dict['repo'] = repo
            post = PostDbIO().create_obj(**form_field_dict)
        ExtraHandler().del_keys(form_field_dict, ('repo', 'content',))
        yaml_content = YAMLHandler().create_yaml(form_field_dict)
        w_yaml_content = ExtraHandler().wrap_content('---', yaml_content)
        full_content = ExtraHandler().join_content(w_yaml_content,
                                                   post.content)
        file_name = ExtraHandler().file_name_f_title(post.title,
                                                     'html')
        FileHandler('/'.join([self.path, '_posts']),
                    file_name).rewrite_file(full_content)

        # Complete all the git operations
        repo = Repo(self.path)
        GithubHandler.commit_all_changes(repo, 'Change site data')
        GithubHandler.push_code(repo, 'gh-pages')
