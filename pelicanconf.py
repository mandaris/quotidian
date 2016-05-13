#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mandaris'
SITENAME = u'Quotidian Quest'
SITEURL = 'http://quotidianquest.com'

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'
LOCALE = u'en_US'

# Site customization
THEME = u'/Users/mandaris/Projects/TuftePelican'
DEBUG = 'TRUE'
STATIC_PATHS = ['images', 'extra', 'code']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# URLs
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ATOM = 'feeds/atom.xml'
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
RELATIVE_URLS = True

# Include plugins
PLUGIN_PATHS = ['/Users/mandaris/Projects/pelican-plugins']
PLUGINS = ['liquid_tags.tufte', 'pelican-open_graph', 'liquid_tags.img']

# Other variables need
SITE_DESCRIPTION = 'The personal website for Mandaris Moore.'
OPEN_GRAPH = True
LOAD_CONTENT_CACHE = False 

