#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2012 Étienne Loks  <etienne.loks_AT_peacefrogsDOTnet>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# See the file COPYING for details.

from django.conf import settings
from django.conf.urls.defaults import *

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()
urlpatterns = patterns('django.views.static',
    (r'^%s(?P<path>.*)' % settings.MEDIA_URL[1:], 'serve',
     {'document_root': settings.MEDIA_ROOT}),
)

if "tinymce" in settings.INSTALLED_APPS:
    urlpatterns += patterns('django.views.static',
        (r'^tinymce/', include('tinymce.urls')),)

urlpatterns += staticfiles_urlpatterns()

urlpatterns += patterns('',
    (r'^trad/', include('rosetta.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^', include('chimere.urls', namespace="chimere")),
)
