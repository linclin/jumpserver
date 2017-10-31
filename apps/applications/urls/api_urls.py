#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from django.conf.urls import url
from rest_framework import routers

from .. import api

app_name = 'applications'

router = routers.DefaultRouter()
router.register(r'v1/terminal/heatbeat', api.TerminalHeatbeatViewSet, 'terminal-heatbeat')
router.register(r'v1/terminal', api.TerminalViewSet, 'terminal')

urlpatterns = [
    url(r'^v1/terminate/connection/$', api.TerminateConnectionView.as_view(),
        name='terminate-connection')
]

urlpatterns += router.urls
