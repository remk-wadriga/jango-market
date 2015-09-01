from django.conf.urls import patterns, url
from market.views import product


urlpatterns = patterns('',
    url(r'^(?P<id>\d+)/$', product.index, name='product_index'),
)
