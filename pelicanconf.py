#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'suno-opnasd'
SITENAME = 'suno-opnasd github pages'
SITEURL = 'https://suno-opnasd.github.io'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'
THEME = './pelican-theme/Flex'

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
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
