#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
AUTHOR = 'Mike'
SITENAME = 'Mike Eder Blog'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme from mcss.mosra.cz
THEME = 'm.css/pelican-theme'
THEME_STATIC_DIR = 'static'
DIRECT_TEMPLATES = ['index']

M_CSS_FILES = ['https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400i,600,600i%7CSource+Code+Pro:400,400i,600',
               '/static/m-dark.css']
M_THEME_COLOR = '#22272e'

PLUGIN_PATHS = ['m.css/pelican-plugins']
PLUGINS = ['m.htmlsanity']

# Theme Nav
M_SITE_LOGO_TEXT = 'Mike Eder'

M_LINKS_NAVBAR2 = [('Blog', 'blog/', '[blog]', [
                        ('News', 'blog/news/', ''),
                        ('Archive', 'blog/archive/', '')]),
                   ('Resume', 'resume/', 'resume', [])]
