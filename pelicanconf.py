#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = 'suno-opnasd'
SITENAME = 'suno-opnasd github pages'
SITEURL = 'https://suno-opnasd.github.io'
SITETITLE = 'Portal'
SITESUBTITLE = 'Suno with Pelican'
SITE_DESCRIPTION = 'hogeee'
PYGMENTS_STYLE = 'github-dark'

ROBOTS = 'index, follow'

PATH = 'content'
# using Flex theme. 
# see also about custom settings -> https://github.com/alexandrevicenzi/Flex/wiki/Custom-Settings
THEME = './pelican-theme/Flex'


TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'
DEFAULT_CATEGORY = 'post'

FILENAME_METADATA = r'(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

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
         )

# Social widget
SOCIAL = (('github', 'https://github.com/suno-opnasd'),
          ('rss', '/feeds/all.atom.xml'),
         )

DEFAULT_PAGINATION = 10

MAIN_MENU = True
HOME_HIDE_TAGS = True
MENUITEMS = (('Posts', '/posts.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

COPYRIGHT_NAME = AUTHOR
COPYRIGHT_YEAR = datetime.now().year
GITHUB_CORNER_URL = 'https://github.com/suno-opnasd/suno-opnasd.gihub.io'
STATIC_PATHS = ['images', 'extra']
CUSTOM_CSS = 'static/custom.css'
#GOOGLE_ADSENSE = {
#
#}
