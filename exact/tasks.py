from __future__ import absolute_import, unicode_literals
from celery import shared_task


import pandas as pd
from itertools import chain
from exact.api import Exact

@shared_task
def inv_view(request):
	e = Exact()

	# first param is the resource.
	# see https://start.exactonline.nl/docs/HlpRestAPIResources.aspx

	# filter returns a generator and handles pagination for you
	data1 = []
	for item in e.filter("inventory/ItemWarehouses",  filter_string=None, select="CurrentStock, ItemCode, ItemDescription"):
		data1.append(item)


	df1 = pd.DataFrame.from_records(data1)

	data2 = []
	for item in e.filter("logistics/Items", filter_string="substringof('LG', ItemGroupCode) eq true and IsSalesItem eq true", select="Stock, PictureThumbnailUrl, Code"):
		data2.append(item)

	df2 = pd.DataFrame.from_records(data2)

	data3 = []
	for item in e.filter("logistics/SalesItemPrices", filter_string="EndDate eq null", select="ItemCode, Price"):
		data3.append(item)


	return render(request, 'exact/inv.html', locals())
