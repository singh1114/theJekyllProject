# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from theJekyllProject.forms import AddPostForm
from django.views.generic.edit import FormView

class AddPostView(FormView):
    """AddPostView to add post

    Example:
        Click on the Add post button when the user is logged in.
        We can add posts only if the user is logged in.

    TODO:
        * Make this view for logged in people only: Not done
        * Load the form: Not Done
        * convert the stuff as required: Not Done
        * Make new files: Not Done
        * Put the files at right places: Not Done
    """
    template_name = 'theJekyllProject/addpost.html'
    form_class = AddPostForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            author = request.POST['author']
            comments = request.POST['comments']
            layout = request.POST['layout']
            title = request.POST['title']
            content = request.POST['content']
            category = request.POST['category']
        return HttpResponseRedirect('/result/' + str(scan_id))

