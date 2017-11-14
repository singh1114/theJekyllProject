from django.conf import settings
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
import re
import shutil
import subprocess

def assign_boolean_to_comments(comments):
    if(comments == 'on'):
        return True
    else:
        return False


def save_post_database(repo, author, comments, date, time, layout, title, content, pk=None):
    if pk is not None:
        post = Post.objects.get(pk=pk)
        post.author = author
        post.comments = comments
        post.date = date
        post.time = time
        post.layout = layout
        post.title = title
        post.content = content
        post.save()
    else:
        post = Post(
            repo=repo,
            author=author,
            comments=comments,
            date=date,
            time=time,
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


def header_content(author=None, comments=None, date=None, time=None, layout=None, title=None):
    string = '---\n'
    if(author is not None):
        string += 'author: ' + author + '\n'
    if(comments is not None):
        comments = str(comments).lower()
        string += 'comments: ' + comments + '\n'
    if(date is not None):
        string += 'date: ' + date
    if(time is not None):
        string += ' ' + time + '\n'
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
    base_dir = settings.BASE_DIR
    file = open(base_dir + '/../JekLog/' + file_name, 'w+')
    file.write(head_content + body_content)
    file.close()


def move_file(file_name, user, repo):
    base_dir = settings.BASE_DIR
    shutil.move(base_dir + '/../JekLog/' + file_name, base_dir + '/../JekLog/' + user.username  + '/' + repo.repo + '/_posts/' + file_name)


def push_online(user, repo):
    base_dir = settings.BASE_DIR
    subprocess.Popen(['/bin/bash', base_dir + '/../' + 'gitsendupstream.sh', user.username, repo.repo, base_dir])


def save_site_data(repo, title=None, description=None, avatar=None):
    site_data = SiteData(
        repo=repo,
        title=title,
        description=description,
        avatar=avatar
    )
    site_data.save()


def save_site_theme_data(repo, theme=None):
    site_theme = SiteTheme(
        repo=repo,
        theme=theme
    )
    site_theme.save()


def create_config_file(user, repo):
    user = User.objects.get(username=user.username)
    try:
        site_data = SiteData.objects.get(repo=repo)

        title = site_data.title
        description = site_data.description
        # FIXME Check avatar properly
        avatar = site_data.avatar
    except:
        title = 'your name'
        description = 'Web Developer from Somewhere'
        # FIXME Create avatar properly
        #avatar = ''

    try:
        site_social_profile = SiteSocialProfile.objects.get(user=user)

        dribbble = site_social_profile.dribbble
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

    try:
        site_theme = SiteTheme.objects.get(user=user)

        theme = site_theme.theme

    except:
        theme = 'jekyll-theme-cayman'

    base_dir = settings.BASE_DIR
    with open(base_dir + '/../' + 'JekLog/' + user.username + '/' + repo.repo + '/' + '_config.yml', 'r') as conf_file:
        file_data = conf_file.read()

    title_data = re.findall(r'name:.+', file_data)
    description_data = re.findall(r'description:.+', file_data)
    avatar_data = re.findall(r'avatar:.+', file_data)

    dribbble_data = re.findall(r'dribbble:.+|dribbble:', file_data)
    email_data = re.findall(r'email:.+|email:', file_data)
    facebook_data = re.findall(r'facebook:.+|facebook:', file_data)
    flickr_data = re.findall(r'flickr:.+|flickr:', file_data)
    github_data = re.findall(r'github:.+|github:', file_data)
    instagram_data = re.findall(r'instagram:.+|instagram:', file_data)
    linkedin_data = re.findall(r'linkedin:.+|linkedin:', file_data)
    pinterest_data = re.findall(r'pinterest:.+|pinterest:', file_data)
    rss_data = re.findall(r'rss:.+|rss:', file_data)
    twitter_data = re.findall(r'twitter:.+|twitter:', file_data)
    stackoverflow_data = re.findall(r'stackoverflow:.+|stackoverflow:', file_data)
    youtube_data = re.findall(r'youtube:.+|youtube:', file_data)
    googleplus_data = re.findall(r'googleplus:.+|googleplus:', file_data)
    disqus_data = re.findall(r'disqus:.+|disqus:', file_data)
    google_analytics_data = re.findall(r'google_analytics:.+|google_analytics:', file_data)

    theme_data = re.findall(r'theme:.+|theme:', file_data)

    file_data = file_data.replace(title_data[0], 'name: ' + title)
    file_data = file_data.replace(description_data[0], 'description: ' + description)
    #file_data = file_data.replace(avatar_data[0], 'avatar: ' + avatar)
    file_data = file_data.replace(dribbble_data[0], 'dribbble: ' + dribbble)
    file_data = file_data.replace(email_data[0], 'email: ' + email)
    file_data = file_data.replace(facebook_data[0], 'facebook: ' + facebook)
    file_data = file_data.replace(flickr_data[0], 'flickr: ' + flickr)
    file_data = file_data.replace(github_data[0], 'github: ' + github)
    file_data = file_data.replace(instagram_data[0], 'instagram: ' + instagram)
    file_data = file_data.replace(linkedin_data[0], 'linkedin: ' + linkedin)
    file_data = file_data.replace(pinterest_data[0], 'pinterest: ' + pinterest)
    file_data = file_data.replace(rss_data[0], 'rss: ' + rss)
    file_data = file_data.replace(twitter_data[0], 'twitter: ' + twitter)
    file_data = file_data.replace(stackoverflow_data[0], 'stackoverflow: ' + stackoverflow)
    file_data = file_data.replace(youtube_data[0], 'youtube: ' + youtube)
    file_data = file_data.replace(googleplus_data[0], 'googleplus: ' + googleplus)
    file_data = file_data.replace(disqus_data[0], 'disqus: ' + disqus)
    file_data = file_data.replace(google_analytics_data[0], 'google_analytics: ' + google_analytics)
    file_data = file_data.replace(theme_data[0], 'theme: ' + theme)

    with open(base_dir + '/../' + 'JekLog/' + user.username + '/' + repo.repo + '/' + '_config.yml', 'w') as conf_file:
        conf_file.write(file_data)


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
    base_dir = settings.BASE_DIR
    dest_path = '/'.join(['JekLog', user.username, repo_name])
    dest_path = base_dir + '/../' + dest_path
    source_path = '/'.join(['JekyllNow', 'jekyll-now'])
    source_path = base_dir + '/../' + source_path
    shutil.copytree(source_path, dest_path)


def add_theme_name(user, repo_name):
    base_dir = settings.BASE_DIR
    with open(base_dir + '/../' + 'JekLog/' + user.username + '/' + repo_name + '/' + '_config.yml', 'a') as conf_file:
        conf_file.write('theme: jekyll-theme-cayman')


def change_site_baseurl(user, repo_name):
    base_dir = settings.BASE_DIR
    with open(base_dir + '/../' +'JekLog/' + user.username + '/' + repo_name + '/' + '_config.yml', 'r') as conf_file:
        filedata = conf_file.read()

    filedata = filedata.replace('baseurl: ""', 'baseurl: "/' + repo_name + '"')

    with open(base_dir + '/../' + 'JekLog/' + user.username + '/' + repo_name + '/' + '_config.yml', 'w') as conf_file:
        conf_file.write(filedata)


def run_git_script(user, repo_name):
    base_dir = settings.BASE_DIR
    user = User.objects.get(username=user.username)
    social = user.social_auth.get(provider='github')
    user_token = social.extra_data['access_token']
    subprocess.Popen(['/bin/bash', base_dir + '/../' + 'gitscript.sh', user.username, repo_name, user_token, base_dir])


def select_main_site(user, pk):
    all_repos = Repo.objects.all()
    current_repo = Repo.objects.get(pk=pk)
    current_repo.main = True
    current_repo.save()
    for repo in all_repos:
        if repo.id is not current_repo.id:
            repo.main = False
            repo.save()
