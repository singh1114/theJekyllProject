# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.views import View

from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.contrib.auth.models import User

from base.handlers.form_handler import FormHandler

from jekyllnow.handlers.jn_form_handlers import InitialFormHandler
from jekyllnow.handlers.jekyllnow_handlers import JekyllNowHandler

from theJekyllProject.choices import BlogTemplates
from theJekyllProject.constants import TemplateName
from theJekyllProject.dbio import RepoDbIO
from theJekyllProject.forms import (
    AddPageForm, AddPostForm, ContactForm, RepoForm, SiteExcludeForm,
    SitePluginForm, SiteProfileForm, SiteThemeForm, SiteSocialProfileForm
)

from theJekyllProject.otherforms.cname_forms import CNameForm

from theJekyllProject.functions import (
    add_theme_name, assign_boolean_to_comments, change_site_baseurl,
    convert_content, copy_jekyll_files, create_config_file, create_file_name,
    create_repo, get_repo_list, header_content, page_header_content,
    push_online, run_git_script, read_all_pages, save_post_database,
    save_page_database, save_post_category_database, save_site_data,
    save_site_theme_data, save_repo_data, select_main_site, write_file,
    write_page_file
)

from theJekyllProject.handlers.cname_handlers import CNameHandler

from theJekyllProject.models import (
    Page, Post, PostCategory, Repo, SiteData, SiteSocialProfile, SiteTheme,
    Contact
)


class IndexView(FormView):
    template_name = 'theJekyllProject/index.html'
    form_class = ContactForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if(form.is_valid()):
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            message = request.POST['message']
            jeklog_email = 'jeklogjek@gmail.com'
            contact = Contact(
                first_name=first_name,
                last_name=last_name,
                email=email,
                message=message
            )
            contact.save()

            subject = ("New mail from " + first_name + " " + last_name + " "
                       + email)
            send_mail(subject, message, email, [jeklog_email],
                      fail_silently=False)

        return render(request, 'theJekyllProject/contact_status.html')


class RepoListView(LoginRequiredMixin, TemplateView):

    def get(self, request, *args, **kwargs):
        user = request.user
        user = User.objects.get(username=user.username)
        social = user.social_auth.get(provider='github')
        user_token = social.extra_data['access_token']

        repo_list = get_repo_list(user_token)

        return render(request, 'theJekyllProject/repo_list.html', context={
            'repo_list': repo_list,
        })


class CreateRepoView(LoginRequiredMixin, FormView):
    template_name = 'theJekyllProject/create_repo.html'
    form_class = RepoForm
    form_valid_message = 'Repository created successfully'
    form_invalid_message = 'Repository not created'

    def get(self, request, *args, **kwargs):
        user = request.user
        user = User.objects.get(username=user.username)
        social = user.social_auth.get(provider='github')
        user_token = social.extra_data['access_token']

        repo_list = get_repo_list(user_token)
        return render(request, 'theJekyllProject/create_repo.html', context={
            'repo_list': repo_list,
            'form': self.form_class,
        })

    def post(self, request, *args, **kwargs):
        """
        This will create a Repo object and and will redirect to choose_template
        """
        form_field_dict = FormHandler(
            request, self.form_class).handle_post_fields((
                'repo',))
        user = request.user
        form_field_dict['user'] = user
        repo = RepoDbIO().create_return(form_field_dict)
        RepoDbIO().update_obj(repo, {'main': True})
        RepoDbIO().change_main(user, repo)
        return HttpResponseRedirect(reverse('choose-template'))

        # form = self.form_class(request.POST)
        # if form.is_valid():
        #     repo = request.POST['repo']
        #
        #     try:
        #         create_repo(user, repo)
        #         save_repo_data(user, repo)
        #         copy_jekyll_files(user, repo)
        #         read_all_pages(user, repo)
        #         add_theme_name(user, repo)
        #         change_site_baseurl(user, repo)
        #         run_git_script(user, repo)
        #     except Exception as error:
        #         raise error
        #
        # return HttpResponseRedirect(reverse('home'))


class ChooseTemplate(LoginRequiredMixin, TemplateView):
    """Choose Template from the list of templates
    """
    def get(self, request, *args, **kwargs):
        return render(request, 'jeklog/choose_template.html')


class AddPostView(LoginRequiredMixin, FormView):
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
        user = request.user
        form = self.form_class(request.POST)
        repo = Repo.objects.get(user=user, main=True)
        if form.is_valid():
            author = request.POST['author']
            comments = request.POST['comments']
            date = request.POST['date']
            time = request.POST['time']
            layout = request.POST['layout']
            title = request.POST['title']
            content = request.POST['content']
            #category = request.POST['category']

            # This is a turnaround... I don't know why it happened.
            # Checkbox produces 'on' as the result when selected.
            comments = assign_boolean_to_comments(comments)

            # save stuff to the post database
            post = save_post_database(repo, author, comments, date, time,
                                      layout, title, content)

            # save stuff to the post_category database
            #save_post_category_database(post, category)

            # Create file name
            file_name = create_file_name(date, title)

            # Create header content for the markdown file
            head_content = header_content(author, comments, date, time,
                                          layout, title)

            # Convert the body content to markdown
            body_content = convert_content(content)

            # Write the content into files
            write_file(user, repo, file_name, head_content, body_content)
            # Push the code online
            push_online(user, repo)
        return HttpResponseRedirect(reverse('home'))


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'theJekyllProject/post_list.html'
    context_object_name = "post_list"

    def get_queryset(self):
        user = self.request.user
        repo = Repo.objects.get(user=user, main=True)
        post_list = Post.objects.order_by('-date').filter(repo=repo)
        return post_list


class PostUpdateView(LoginRequiredMixin, FormView):
    form_class = AddPostForm
    template_name = 'theJekyllProject/addpost.html'

    def get_form_kwargs(self):
        pk = self.kwargs['pk']
        try:
            post = Post.objects.get(pk=pk)
            author = post.author
            comments = post.comments
            date = post.date
            time = post.time
            layout = post.layout
            title = post.title
            content = post.content
            # FIXME get is used as we can only category for now
            #post_category = PostCategory.objects.get(post=post)
            #category = post_category.category
        except:
            pass

        form_kwargs = super(PostUpdateView, self).get_form_kwargs()
        form_kwargs.update({
            'initial': {
                'author': author,
                'comments': comments,
                'date': date,
                'time': time,
                'layout': layout,
                'title': title,
                'content': content,
                #'category': category
            }
        })
        return form_kwargs

    def post(self, request, *args, **kwargs):
        user = request.user
        pk = self.kwargs['pk']
        form = self.form_class(request.POST)
        repo = Repo.objects.get(user=user, main=True)
        if form.is_valid():
            author = request.POST['author']
            comments = request.POST['comments']
            date = request.POST['date']
            time = request.POST['time']
            layout = request.POST['layout']
            title = request.POST['title']
            content = request.POST['content']
            #category = request.POST['category']

            # This is a turnaround... I don't know why it happened.
            # Checkbox produces 'on' as the result when selected.
            comments = assign_boolean_to_comments(comments)

            # save stuff to the post database
            post = save_post_database(repo, author, comments, date, time,
                                      layout, title, content, pk)

            # save stuff to the post_category database
            #save_post_category_database(post, category, pk)

            file_name = create_file_name(date, title)

            # Create header content for the markdown file
            head_content = header_content(author, comments, date, time, layout,
                                          title)

            # Convert the body content to markdown
            body_content = convert_content(content)

            # Write the content into files
            write_file(user, repo, file_name, head_content, body_content)

            # send the changes online
            push_online(user, repo)
        return HttpResponseRedirect(reverse('home'))


class AddPageView(LoginRequiredMixin, FormView):
    """AddPageView to add page

    Example:
        Click on the Add page button when the user is logged in.
        We can add pages only if the user is logged in.

    Tasks:
        * Make this view for logged in people only.
        * Load the form:
        * convert the taken html to markdown
        * create and move the files to proper locations
        * Push the code to the repository.
    """
    template_name = 'theJekyllProject/addpage.html'
    form_class = AddPageForm

    def post(self, request, *args, **kwargs):
        user = request.user
        form = self.form_class(request.POST)
        repo = Repo.objects.get(user=user, main=True)
        if form.is_valid():
            title = request.POST['title']
            permalink = request.POST['permalink']
            content = request.POST['content']

            # save stuff to the page database
            save_page_database(repo, title, permalink, content)

            # Create header content for the markdown file
            head_content = page_header_content(title, permalink)

            # Convert the body content to markdown
            body_content = convert_content(content)

            # Write the content into files
            write_page_file(title.lower(), user, repo, head_content,
                            body_content)

            # Push the code online
            push_online(user, repo)
        return HttpResponseRedirect(reverse('page-list'))


class PageUpdateView(LoginRequiredMixin, FormView):
    """PageUpdateView to add page

    Example:
        Click on any of the page when the user is logged in.
        We can update the content of pages only if the user is logged in.

    Tasks:
        * Make this view for logged in people only.
        * Load the form with content from the database
        * convert the taken html to markdown
        * create and move the files to proper locations
        * Push the code to the repository
    """
    form_class = AddPageForm
    template_name = 'theJekyllProject/addpage.html'

    def get_form_kwargs(self):
        pk = self.kwargs['pk']
        try:
            page = Page.objects.get(pk=pk)
            title = page.title
            permalink = page.permalink
            content = page.content
        except:
            pass

        form_kwargs = super(PageUpdateView, self).get_form_kwargs()
        form_kwargs.update({
            'initial': {
                'title': title,
                'permalink': permalink,
                'content': content,
            }
        })
        return form_kwargs

    def post(self, request, *args, **kwargs):
        user = request.user
        pk = self.kwargs['pk']
        form = self.form_class(request.POST)
        repo = Repo.objects.get(user=user, main=True)
        if form.is_valid():
            title = request.POST['title']
            permalink = request.POST['permalink']
            content = request.POST['content']

            save_page_database(repo, title, permalink, content, pk)

            # Create header content for the markdown file
            head_content = page_header_content(title, permalink)

            # Convert the body content to markdown
            body_content = convert_content(content)

            # Write the content into files
            write_page_file(title.lower(), user, repo, head_content,
                            body_content)

            # Push the code online
            push_online(user, repo)
        return HttpResponseRedirect(reverse('page-update', args=[pk]))


class PageListView(LoginRequiredMixin, ListView):
    model = Page
    template_name = 'theJekyllProject/page_list.html'
    context_object_name = "page_list"

    def get_queryset(self):
        user = self.request.user
        repo = Repo.objects.get(user=user, main=True)
        page_list = Page.objects.filter(repo=repo)
        return page_list


class SiteProfileView(LoginRequiredMixin, FormView):
    template_name = 'theJekyllProject/siteprofile.html'
    form_class = SiteProfileForm

    def get(self, request, *args, **kwargs):
        """
        get will load the initials if they are present in the db.
        """
        form = InitialFormHandler(self.request.user,
            self.form_class).load_jn_site_initials()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user
            name = request.POST['name']
            description = request.POST['description']
            avatar = request.POST['avatar']

            repo = RepoDbIO().get_obj({
                'user': self.request.user,
                'main': True,
            })
            data_dict = {
                'repo': repo,
                'name': name,
                'description': description,
                'avatar': avatar
            }
            JekyllNowHandler(request.user, repo.repo).perform_site_data(
                data_dict)
            return HttpResponseRedirect(reverse('home'))


class ChooseSiteView(LoginRequiredMixin, ListView):
    model = Repo
    template_name = 'theJekyllProject/choose_site.html'
    context_object_name = 'site_list'

    def get_queryset(self):
        site_list = Repo.objects.filter(user=self.request.user)
        return site_list


class SelectMainSiteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        user = self.request.user
        select_main_site(user, pk)
        return HttpResponseRedirect(reverse('home'))


class DecideHomeView(View):
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect(reverse('index'))
        user = self.request.user
        repo = Repo.objects.filter(user=user, main=True)
        if not repo.exists():
            return redirect(reverse('create-repo'))
        elif str(repo.first().template) == str(BlogTemplates.TEMPLATE_NOT_SET):
            return redirect(reverse('choose-template'))
        else:
            return redirect(reverse('home'))


class SiteSocialProfileView(LoginRequiredMixin, FormView):
    template_name = 'theJekyllProject/socialprofile.html'
    form_class = SiteSocialProfileForm

    def get_form_kwargs(self):
        user = self.request.user
        user = User.objects.get(username=user.username)
        try:
            SiteSocialProfile.objects.get(user=user)
            dribbble = SiteSocialProfile.objects.get(user=user).dribbble
            email = SiteSocialProfile.objects.get(user=user).email
            facebook = SiteSocialProfile.objects.get(user=user).facebook
            flickr = SiteSocialProfile.objects.get(user=user).flickr
            github = SiteSocialProfile.objects.get(user=user).github
            instagram = SiteSocialProfile.objects.get(user=user).instagram
            linkedin = SiteSocialProfile.objects.get(user=user).linkedin
            pinterest = SiteSocialProfile.objects.get(user=user).pinterest
            rss = SiteSocialProfile.objects.get(user=user).rss
            twitter = SiteSocialProfile.objects.get(user=user).twitter
            stackoverflow = SiteSocialProfile.objects.get(
                user=user
            ).stackoverflow
            youtube = SiteSocialProfile.objects.get(user=user).youtube
            googleplus = SiteSocialProfile.objects.get(user=user).googleplus
            disqus = SiteSocialProfile.objects.get(user=user).disqus
            google_analytics = SiteSocialProfile.objects.get(
                user=user
            ).google_analytics
        except:
            dribbble = ''
            email = ''
            facebook = ''
            flickr = ''
            github = ''
            instagram = ''
            linkedin = ''
            pinterest = ''
            rss = ''
            twitter = ''
            stackoverflow = ''
            youtube = ''
            googleplus = ''
            disqus = ''
            google_analytics = ''

        form_kwargs = super(SiteSocialProfileView, self).get_form_kwargs()
        form_kwargs.update({
            'initial': {
                'dribbble': dribbble,
                'email': email,
                'facebook': facebook,
                'flickr': flickr,
                'github': github,
                'instagram': instagram,
                'linkedin': linkedin,
                'pinterest': pinterest,
                'rss': rss,
                'twitter': twitter,
                'stackoverflow': stackoverflow,
                'youtube': youtube,
                'googleplus': googleplus,
                'disqus': disqus,
                'google_analytics': google_analytics,
            }
        })
        return form_kwargs

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user
            repo = Repo.objects.get(user=user, main=True)
            dribbble = request.POST['dribbble']
            email = request.POST['email']
            facebook = request.POST['facebook']
            flickr = request.POST['flickr']
            github = request.POST['github']
            instagram = request.POST['instagram']
            linkedin = request.POST['linkedin']
            pinterest = request.POST['pinterest']
            rss = request.POST['rss']
            twitter = request.POST['twitter']
            stackoverflow = request.POST['stackoverflow']
            youtube = request.POST['youtube']
            googleplus = request.POST['googleplus']
            disqus = request.POST['disqus']
            google_analytics = request.POST['google_analytics']

            site_social_profile = SiteSocialProfile(
                user=user,
                dribbble=dribbble,
                email=email,
                facebook=facebook,
                flickr=flickr,
                github=github,
                instagram=instagram,
                linkedin=linkedin,
                pinterest=pinterest,
                rss=rss,
                twitter=twitter,
                stackoverflow=stackoverflow,
                youtube=youtube,
                googleplus=googleplus,
                disqus=disqus,
                google_analytics=google_analytics
            )
            site_social_profile.save()
            create_config_file(user, repo)
            push_online(user, repo)
            return HttpResponseRedirect(reverse('socialprofile'))


class SitePluginView(LoginRequiredMixin, FormView):
    template_name = 'theJekyllProject/siteplugin.html'
    form_class = SitePluginForm


class SiteExcludeView(LoginRequiredMixin, FormView):
    template_name = 'theJekyllProject/siteexclude.html'
    form_class = SiteExcludeForm


class SiteThemeView(LoginRequiredMixin, FormView):
    template_name = 'theJekyllProject/sitetheme.html'
    form_class = SiteThemeForm

    def get_form_kwargs(self):
        user = self.request.user
        user = User.objects.get(username=user.username)
        try:
            SiteTheme.objects.get(user=user)
            theme = SiteTheme.objects.get(user=user).theme
        except ObjectDoesNotExist:
            theme = ''

        form_kwargs = super(SiteThemeView, self).get_form_kwargs()
        form_kwargs.update({
            'initial': {
                'theme': theme,
            }
        })
        return form_kwargs

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = request.user
            repo = Repo.objects.get(user=user, main=True)
            theme = request.POST['theme']
            save_site_theme_data(repo, theme)
            create_config_file(user, repo)
            push_online(user, repo)
            return HttpResponseRedirect(reverse('sitetheme'))


class BlogView(LoginRequiredMixin, View):
    """BlogView to see the created blog

    Example:
        Triggers when:
        User clicks on the visit the blog button when logged in
        This will take you to the Existing blog

    Tasks:
        * View for logged in users only.
        * Place the link in the user options
        * Redirect to the correct link.
        * If the repo_name is equal to username.github.io
          then redirect to username.github.io only
    """
    def get(self, request, *args, **kwargs):
        user = request.user
        repo = Repo.objects.get(user=user, main=True)
        if(repo.repo != (user.username + '.github.io')):
            return redirect('http://' + user.username +
                            '.github.io/' + repo.repo)
        else:
            return redirect('http://' + user.username + '.github.io/')


class CNameView(LoginRequiredMixin, FormView):
    """
    CNAMEView is used to setup the cname for the repo choosen
    """
    form_class = CNameForm

    def get(self, request, *args, **kwrags):
        """
        Take the value of the CNAME from the db and return to the frontend
        """
        user = request.user
        response = CNameHandler().load_initials(user, self.form_class)

        return render(request, TemplateName.CNAME_TEMPLATE, {'form': response})

    def post(self, request, *args, **kwargs):
        """
        Accepts the cname from the field and add into the database
        """
        user = request.user
        form_field_dict = FormHandler(request,
            self.form_class).handle_post_fields(('cname',))
        CNameHandler().assign_cname(user, form_field_dict['c_name'])
        return render(request, TemplateName.CNAME_TEMPLATE,
            {'msg': 'CNAME updated successfully.'})
