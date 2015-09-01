from django.conf.urls import patterns, url
from market.views import landing


urlpatterns = patterns('/',
    url(r'^$', landing.index, name='main_page'),
)
