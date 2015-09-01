from django.conf.urls import patterns, url
from market.views import landing


urlpatterns = patterns('/',
    url(r'^$', landing.index, name='index'),
    url(r'^catalog/$', landing.CatalogView.as_view(), name='catalog'),
)
