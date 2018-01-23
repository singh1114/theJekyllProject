[![Build Status](https://travis-ci.org/singh1114/theJekyllProject.svg?branch=master)](https://travis-ci.org/singh1114/theJekyllProject)
# JekLog
A Django project to create blogs using django Content Management System. 
[JekLog](http://jeklog.com)

## Usage

- Blog Tutorial:
	[http://blog.jeklog.com/how-to-create-a-free-blog-using-github-pages-and-jekyll-with-jeklog/](http://blog.jeklog.com/how-to-create-a-free-blog-using-github-pages-and-jekyll-with-jeklog/)
- YouTube Video: 
	[![Tutorial Video](https://img.youtube.com/vi/6SnaarQlRsw/0.jpg)](https://www.youtube.com/watch?v=6SnaarQlRsw)

## System requirements

- Python 2.7+
- PostgreSQL 9.5+: `sudo apt-get install postgresql-9.5-dev`

## Database Instructions

- `sudo -i -u postgres`
- `psql`

- `create database your_database_name`

Now change the content of the file settings.py accordingly.


### Documentation

#### How to install and use

We use `virtualenv` for the python installation process. This is the recommended way of installing.

- Use the following link for the installation process.

[Virtual environment installation](http://singh1114.github.io/blog/how-to-install-django-using-virtual-environment/)

After this, you need to get the code using fork and `git clone`

Fork and clone the code using the following command.

```sudo apt-get install git```

```$ git clone https://github.com/your_gh_username/theJekyllProject```

```$ cd theJekyllProject```

While in the virtual environment, use the following command to install the requirements

```$ pip install -r requirements.txt```

Now you need to get tokens for the github app. Create the tokens with proper callback URI and add both things to `djangoFiles/djangoFiles/settings.py`. 

After this you need to create the database. For this use the following command

This command will create jeklog user. Enter `jeklog` as the password as well. You can choose some other name and change the configuration settings in the `djangoFiles/djangoFiles/settings.py`

```sudo -u postgres createuser --no-createrole --no-superuser --login --inherit --createdb --pwprompt jeklog```

After this create a database named jeklog with the created user, using the following command.

```createdb --encoding=utf-8 --owner=jeklog --user=jeklog --password --host=localhost --port=5432 jeklog```

Now start the server and hopefully, everything will work without any error. If some error occurs, let us know.

### Future Scope

We are going to use environment variables for settings file. `Direnv` is a good tool for this purpose. 

We are going to build a proper useable server for the admin users. So that you guys can run it on your system.