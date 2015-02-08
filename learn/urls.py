from django.conf.urls import patterns, include, url

from learn.views import *

urlpatterns = patterns('',
    url(r'^$', index,name='index'),
    url(r'^add/$', add,name='add'),
    url(r'^add/(\d+)/(\d+)/$', add2,name='add2'),
)
