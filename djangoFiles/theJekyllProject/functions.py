from theJekyllProject.models import Post

import html2markdown


def assign_boolean_to_comments(comments):
    if(comments == 'on'):
        return True
    else:
        return False


def save_post_database(author, comments, date, layout, title, content):
    post = Post(
        author=author,
        comments=comments,
        date=date,
        layout=layout,
        title=title,
        content=content,
    )
    post.save()


def create_file_name(date, title):
    date_to_string = str(date)
    title = title.lower()
    title = title.replace(' ', '-')
    file_name = str(date) + '-' + title + '.markdown'
    print file_name
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
