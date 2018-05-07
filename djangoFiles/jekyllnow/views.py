# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views import View

from base.handlers.extra_handlers import ExtraHandler

from jekyllnow.handlers.jekyllnow_handlers import JekyllNowHandler


class JekyllNowTheme(LoginRequiredMixin, View):
    """
    Does the primary tasks and redirect to site route.
    """
    def get(self, request, *args, **kwargs):
        user = self.request.user
        repo = ExtraHandler().main_repo_with_no_template(user)
        jekyll_now = JekyllNowHandler(user, repo)
        jekyll_now.perform_initial_tasks()
        return HttpResponseRedirect(reverse('siteprofile'))
