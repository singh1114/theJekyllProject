# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from base.handlers.form_handler import FormHandler

from startbootstrap.handlers import StartBootstrapHandler

class StartBootstrapThemeView(LoginRequiredMixin, View):
    """
    First view that will do all preliminary operations for setting up the repo
    """
    def post(self, request, *args, **kwargs):
        """
        Handle the post data. Ideally, reponame will be posted
        """
        user = self.request.user
        form_field_dict = FormHandler(request,
            self.form_class).handle_post_fields(('repo',))

        start_bootstrap = StartBootstrapHandler(user, form_field_dict['repo'])

        start_bootstrap.perform_initial_tasks()
