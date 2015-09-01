from django.conf.urls import patterns, url
from market.views import category

urlpatterns = patterns('',
    url(r'^(?P<id>\d+)/products/$', category.products_list, name='category_products_list'),
)
