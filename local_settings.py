#!/usr/bin/env python
# -*- coding: utf-8 -*-

# rename this file to local_settings.py and overload settings in this file

import os

ROOT_PATH = os.path.realpath(os.path.dirname(__file__))

STATIC_URL = '/static/'

CHIMERE_OSM_API_URL = 'api06.dev.openstreetmap.org' # test URL
CHIMERE_OSM_USER = 'osm_user'
CHIMERE_OSM_PASSWORD = 'osm_pass'
CHIMERE_SHARE_NETWORKS = []

# Make this string unique, and don't share it with anybody.
SECRET_KEY = "gziu+84j0$8-n6u$!@q$5yevh=8gm!)#*vc9ghj7s9g1rlg#r8"

ADMINS = (
    ('Alban Tiberghien', 'albantiberghien@imaginatioforpeople.org'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'NAME': 'chimere_dakar',
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'chimere_dakar',
        'PASSWORD': 'chimere_dakar',
    },
}


ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(ROOT_PATH, 'templates/'),
)

CHIMERE_FEEDS = False
EMAIL_HOST = False

TINYMCE_URL = '%stiny_mce/' % STATIC_URL
JQUERY_JS_URLS = ("https://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js",
                  'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.23/jquery-ui.min.js')
JQUERY_CSS_URLS = ('https://ajax.googleapis.com/ajax/libs/jqueryui/1.8/themes/base/jquery-ui.css',)
