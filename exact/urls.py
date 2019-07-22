# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from .views import Authenticate, Status, webhook, financials_view, inv_view, index

urlpatterns = [
	url(r'^authenticate$', Authenticate.as_view(), name="authenticate"),
	url(r'^status', Status.as_view(), name="status"),
	url(r'^inv', inv_view, name="inv"),
	url(r'^tables', tables_view, name="tables"),
	url(r'^financials', financials_view, name="financials"),
	url(r'^webhook', webhook, name="webhook"),
	url(r'^$', index, name='index'),
]
