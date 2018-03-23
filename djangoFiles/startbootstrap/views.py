# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.edit import FormView

from base.handlers.form_handler import FormHandler

from startbootstrap.constants import TemplateName
from startbootstrap.dbio import SiteDataDbIO
from startbootstrap.forms import SiteProfileForm
from startbootstrap.handlers.sbs_handlers import SBSHandler

from theJekyllProject.dbio import RepoDbIO


class StartBootstrapThemeView(LoginRequiredMixin, View):
    """
    First view that will do all preliminary operations for setting up the
    startbootstrap blog.
    """
    def post(self, request, *args, **kwargs):
        """
        Handle the post data. Ideally, reponame will be posted
        """
        # TODO Add the intial db filling code
        user = self.request.user
        repo = request.data.get('repo')
        start_bootstrap = SBSHandler(user, repo)
        start_bootstrap.perform_initial_tasks()
        return HttpResponseRedirect(reverse('site-data'))


class SBSDataView(LoginRequiredMixin, FormView):
    """
    Form View to handle site data of the startbootstrap theme
    """
    form_class = SiteProfileForm

    def get(self, request, *args, **kwargs):
        response = SBSHandler.load_site_initials(
            request.user, self.form_class)

        return render(request, TemplateName.SBS_SITE_DATA, {'form': response})

    def post(self, request, *args, **kwargs):
        # TODO create the _config.yml file commit and push the changes
        form_field_dict = FormHandler(
            request, self.form_class).handle_post_fields((
                'title',
                'description',
                'author',
                'baseurl')
        )
        user = request.user
        RepoDbIO().get_repo(user)
        SiteDataDbIO().create_obj({
            'title': form_field_dict['title'],
            'description': form_field_dict['description'],
            'author': form_field_dict['author'],
            'baseurl': form_field_dict['baseurl']
        })

        return render(request, TemplateName.SBS_SITE_DATA,
                      {'msg': 'Site data updated successfully.'})
