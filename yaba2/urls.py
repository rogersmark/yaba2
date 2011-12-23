from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from yaba2.views import StoryListView

urlpatterns = patterns('',
    url(r'^$', StoryListView.as_view(), name='index'),
    url(r'^tag/(?P<tag_name>[\w_-]+)/$',
        StoryListView.as_view(),
        name='tag-stories'
    ),
)

urlpatterns += staticfiles_urlpatterns()
