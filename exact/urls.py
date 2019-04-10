# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import url

from .views import Authenticate, Status, webhook, documents_view, logistics_view, financials_view, attachments_view, itemgroup_view, inv_view, index

urlpatterns = [
	url(r'^authenticate$', Authenticate.as_view(), name="authenticate"),
	url(r'^status', Status.as_view(), name="status"),
	url(r'^documents', documents_view, name="docu"),
	url(r'^attachments', attachments_view, name="attachments"),
	url(r'^logistics', logistics_view, name="logistics"),
	url(r'^itemgroup', itemgroup_view, name="itemgroup"),
	url(r'^inv', inv_view, name="inventorywarehouse"),
	url(r'^financials', financials_view, name="financials"),
	url(r'^webhook', webhook, name="webhook"),
	url(r'^.*$', index, name='index'),
]
