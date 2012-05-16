"""
raven.contrib.django.urls
~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2010-2012 by the Sentry Team, see AUTHORS for more details.
:license: BSD, see LICENSE for more details.
"""

from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^report/', 'raven.contrib.django.views.report'),
)
