from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import DetailView

from yaba2 import models
from yaba2.views import StoryListView

urlpatterns = patterns('',
    url(r'^$', StoryListView.as_view(), name='index'),
    url(r'^tag/(?P<tag_name>[\w_-]+)/$',
        StoryListView.as_view(),
        name='tag-stories'
    ),
    url(r'^post/(?P<slug>[\w_-]+)/$', DetailView.as_view(
        model=models.Story,
        context_object_name='story')
    ),
)

urlpatterns += staticfiles_urlpatterns()
