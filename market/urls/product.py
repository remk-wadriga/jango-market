from django.conf.urls import patterns, url
from market.views import product


urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/$', product.IndexView.as_view(), name='index'),
)
