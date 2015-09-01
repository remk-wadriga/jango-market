from django.conf.urls import patterns, url
from market.views import category

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/products/$', category.ProductsView.as_view(), name='products'),
)
