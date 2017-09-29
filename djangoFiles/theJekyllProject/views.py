# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime
from django.shortcuts import render
from django.views.generic.edit import FormView

from markdown2 import Markdown

from theJekyllProject.forms import AddPostForm
from theJekyllProject.functions import assign_boolean_to_comments
from theJekyllProject.functions import save_post_database
from theJekyllProject.functions import create_file_name
from theJekyllProject.functions import header_content
from theJekyllProject.functions import convert_content
from theJekyllProject.functions import write_file

from theJekyllProject.models import Post


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
            date = request.POST['date']
            layout = request.POST['layout']
            title = request.POST['title']
            content = request.POST['content']
            category = request.POST['category']

            # This is a turnaround... I don't know why it happened.
            # Checkbox produces 'on' as the result when selected.
            comments = assign_boolean_to_comments(comments)

            # save stuff to the database
            save_post_database(author, comments, date, layout, title, content)

            # Create file name
            date_obj = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            only_date = date_obj.date()
            file_name = create_file_name(only_date, title)

            # Create header content for the markdown file
            head_content = header_content(author, comments, date, layout, title)

            # Convert the body content to markdown
            body_content = convert_content(content)

            # Write the content into files
            write_file(file_name, head_content, body_content)

        return HttpResponseRedirect('/result/' + str(scan_id))

