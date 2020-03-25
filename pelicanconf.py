#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mandaris'
AUTHOR_NOTE = u'Mandaris is someone who strives to make himself into a better person'
AUTHOR_URL = u'https://mandarismoore.com'
AUTHOR_IMAGE = u'https://secure.gravatar.com/avatar/03fb367dd4c7aea56f77dfa496db3725'

SITENAME = u'Mandaris Moore'
SITEURL = 'https://mandarismoore.com'

TWITTER_USERNAME = 'mandaris'
GITHUB_USERNAME = 'mandaris'
WEBMENTION = 'mandarismoore.com'
#FACEBOOK_PROFILE_URL = 'something'
MICROBLOG_USERNAME = 'mandaris'

PATH = '../chronicles'
OUTPUT_PATH = '/var/www/html/mandarismoore.com/public_html'

TIMEZONE = 'US/Pacific'
SITE_DESCRIPTION = 'The personal website for Mandaris Moore.'
DEFAULT_LANG = u'en-US'
LOCALE = u'en_US'
DEFAULT_PAGINATION = 10

# Site customization
THEME = u'../Modest' #Change to needed
DISPLAY_PAGES_ON_MENU = True
STATIC_PATHS = ['images', 'extra', 'code']
EXTRA_PATH_METADATA = {'extra/favicon.png': {'path': 'favicon.png'},
                       'extra/apple-touch-icon.png': {'path': 'apple-touch-icon.png'},
                       'extra/apple-touch-icon-precomposed.png': {'path': 'apple-touch-icon-precomposed.png'},
                       'extra/favicon.ico': {'path': 'favicon.ico'},}

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
PLUGINS = ['liquid_tags.tufte', 'pelican-open_graph', 'liquid_tags.img']

# Markdown Plugins
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {'baselevel': '3', 'title': 'Table of Contents'},
        # 'figureAltCaption':{},
    },
    'output_format': 'html5',
}

# Other variables 
OPEN_GRAPH = True
LOAD_CONTENT_CACHE = False 
#DISQUS_SITENAME = r'mandarismoore.com'
FAVICON_ALT = u'A person in a gear.'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
#DEBUG = True
