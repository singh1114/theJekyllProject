from django.contrib.auth.models import User

from theJekyllProject.models import Post
from theJekyllProject.models import PostCategory
from theJekyllProject.models import SiteData
from theJekyllProject.models import SiteSocialProfile
from theJekyllProject.models import SiteTheme
from theJekyllProject.models import Repo

from github import Github

import html2markdown
import os
import shutil
import subprocess


def assign_boolean_to_comments(comments):
    if(comments == 'on'):
        return True
    else:
        return False


def save_post_database(user, author, comments, date, layout, title, content, pk=None):
    if pk is not None:
        post = Post.objects.get(pk=pk)
        post.author = author
        post.comments = comments
        post.date = date
        post.layout = layout
        post.title = title
        post.content = content
        post.save()
    else:
        post = Post(
            user=user,
            author=author,
            comments=comments,
            date=date,
            layout=layout,
            title=title,
            content=content,
        )
        post.save()
    return post


def save_post_category_database(post, category, pk=None):
    if pk is not None:
        # FIXME use filter instead of get
        post = Post.objects.get(pk=pk)
        post_category = PostCategory.objects.get(post=post)
        post_category.category = category
        post_category.save()
    else:
        post_category = PostCategory(
            post=post,
            category=category
        )
        post_category.save()


def create_file_name(date, title):
    date_to_string = str(date)
    title = title.lower()
    title = title.replace(' ', '-')
    file_name = str(date) + '-' + title + '.markdown'
    return file_name


def header_content(author=None, comments=None, date=None, layout=None, title=None):
    string = '---\n'
    if(author is not None):
        string += 'author: ' + author + '\n'
    if(comments is not None):
        comments = str(comments).lower()
        string += 'comments: ' + comments + '\n'
    if(date is not None):
        string += 'date: ' + date + '\n'
    if(layout is not None):
        string += 'layout: ' + layout + '\n'
    if(title is not None):
        string += 'title: ' + title + '\n'
        title = title.lower()
        slug = title.replace(' ', '-')
        string += 'slug: ' + slug + '\n'
    string += '---\n'

    return string


def convert_content(content):
    return html2markdown.convert(content)


def write_file(file_name, head_content, body_content):
    file = open(file_name, 'w+')
    file.write(head_content + body_content)
    file.close()


def move_file(file_name, user, repo):
    shutil.move(file_name, 'JekLog/' + user.username  + '/' + repo.repo + '/_posts/' + file_name)


def push_online(user, repo):
    subprocess.Popen(['/bin/bash', 'gitsendupstream.sh', user.username, repo.repo])


def save_site_data(user, title=None, description=None, avatar=None):
    site_data = SiteData(
        user=user,
        title=title,
        description=description,
        avatar=avatar
    )
    site_data.save()


def save_site_theme_data(user, theme=None):
    site_theme = SiteTheme(
        user=user,
        theme=theme
    )
    site_theme.save()

# FIXME How can we only change the certain part of the file rather than changing the whole file.
def create_config_file(user):
    user = User.objects.get(username=user.username)
    try:
        site_data = SiteData.objects.get(user=user)

        title = site_data.title
        description = site_data.description
        # FIXME Check avatar properly
        avatar = site_data.avatar
    except:
        title = ''
        description = ''
        # FIXME Create avatar properly
        #avatar = ''

    # create string
    file_string = '# first phase starts\n'
    file_string += 'title: ' + title + '\n'
    file_string += 'description: ' + description + '\n'
    # We have to create the github URL of the avatar
    #file_string += 'avatar: ' + avatar + '\n'
    file_string += '# first phase ends\n'

    try:
        site_social_profile = SiteSocialProfile.objects.get(user=user)

        dribble = site_social_profile.dribble
        email = site_social_profile.email
        facebook = site_social_profile.facebook
        flickr = site_social_profile.flickr
        github = site_social_profile.github
        instagram = site_social_profile.instagram
        linkedin = site_social_profile.linkedin
        pinterest = site_social_profile.pinterest
        rss = site_social_profile.rss
        twitter = site_social_profile.twitter
        stackoverflow = site_social_profile.stackoverflow
        youtube = site_social_profile.youtube
        googleplus = site_social_profile.googleplus
        disqus = site_social_profile.disqus
        google_analytics = site_social_profile.google_analytics

    except:
            dribble = ''
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


    file_string += '# second phase starts\n'
    file_string += 'dribble: ' +  dribble + '\n'
    file_string += 'email: ' +  email + '\n'
    file_string += 'facebook: ' +  facebook + '\n'
    file_string += 'flickr: ' +  flickr + '\n'
    file_string += 'github: ' +  github + '\n'
    file_string += 'instagram: ' +  instagram + '\n'
    file_string += 'linkedin: ' +  linkedin + '\n'
    file_string += 'pinterest: ' +  pinterest + '\n'
    file_string += 'rss: ' +  rss + '\n'
    file_string += 'twitter: ' +  twitter + '\n'
    file_string += 'stackoverflow: ' +  stackoverflow + '\n'
    file_string += 'youtube: ' +  youtube + '\n'
    file_string += 'googleplus: ' +  googleplus + '\n'
    file_string += 'disqus: ' +  disqus + '\n'
    file_string += 'google_analytics: ' +  google_analytics + '\n'
    file_string += '# second phase ends\n'

    try:
        site_theme = SiteTheme.objects.get(user=user)

        theme = site_theme.theme

    except:
        theme = ''

    file_string += '# third phase starts\n'
    file_string += 'theme: ' + theme + '\n'
    file_string += '# third phase ends\n'
    file = open('_config.yml', 'w')
    file.write(file_string)
    file.close()
    shutil.move('_config.yml', 'theJekyllProject/_config.yml')


def get_repo_list(token):
    g = Github(token)
    repositories_name = []
    for repo in g.get_user().get_repos():
        repositories_name.append(repo.name)
    return repositories_name


def save_repo_data(user, repo):
    repo = Repo(
        user=user,
        repo=repo,
        main=True
    )
    repo.save()

    # Now set all other repo `main` to False
    all_repos = Repo.objects.all()
    current_repo = Repo.objects.get(id=repo.id)
    for repo in all_repos:
        if repo.id is not current_repo.id:
            repo.main = False
            repo.save()


def create_repo(user, repo):
    user = User.objects.get(username=user.username)
    social = user.social_auth.get(provider='github')
    user_token = social.extra_data['access_token']
    g = Github(user_token)
    user = g.get_user()
    repo = user.create_repo(repo)


def copy_jekyll_files(user, repo_name):
    print user.username
    print repo_name
    dest_path = '/'.join(['JekLog', user.username, repo_name])
    source_path = '/'.join(['JekyllNow', 'jekyll-now'])
    shutil.copytree(source_path, dest_path)


def run_git_script(user, repo_name):
    user = User.objects.get(username=user.username)
    social = user.social_auth.get(provider='github')
    user_token = social.extra_data['access_token']
    subprocess.Popen(['/bin/bash', 'gitscript.sh', user.username, repo_name, user_token])


def select_main_site(user, pk):
    all_repos = Repo.objects.all()
    current_repo = Repo.objects.get(pk=pk)
    current_repo.main = True
    current_repo.save()
    for repo in all_repos:
        if repo.id is not current_repo.id:
            repo.main = False
            repo.save()
