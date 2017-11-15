#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mandaris'
SITENAME = u'Quotidian Quest'
SITEURL = 'http://quotidianquest.com'

PATH = 'content'

TIMEZONE = 'US/Pacific'
SITE_DESCRIPTION = 'The personal website for Mandaris Moore.'
DEFAULT_LANG = u'en'
LOCALE = u'en_US'
DEFAULT_PAGINATION = 10

# Site customization
THEME = u'../../Projects/yapeme' #Change to needed
DEFAULT_OG_IMAGE = "/favicon.png"
DISPLAY_PAGES_ON_MENU = True
STATIC_PATHS = ['images', 'extra', 'code']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},
                       'extra/favicon.ico': {'path': 'favicon.ico'},
                       'extra/favicon.png': {'path': 'favicon.png'},
                       'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},}

## URLs
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'

## Feed generation (usually not desired when developing)
FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ATOM = 'feeds/atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Include plugins
PLUGIN_PATHS = ['../../Projects/pelican-plugins']
PLUGINS = ['i18n_subsites', 'liquid_tags.tufte', 'pelican-open_graph', 'liquid_tags.img', 'plantuml', 'assets', ]

# Markdown Plugins
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

# Other variables 
OPEN_GRAPH = True
LOAD_CONTENT_CACHE = False 

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
#DEBUG = True
