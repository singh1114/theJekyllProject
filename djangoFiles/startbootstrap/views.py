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
from startbootstrap.forms import SiteProfileForm
from startbootstrap.handlers.sbs_handlers import SBSHandler
from startbootstrap.handlers.sbs_form_handlers import SBSFormHandler


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
        response = SBSFormHandler.load_site_initials(
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
        SBSFormHandler().post_site_data(user, form_field_dict)

        return render(request, TemplateName.SBS_SITE_DATA,
                      {'msg': 'Site data updated successfully.'})
