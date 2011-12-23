from django.conf.urls.defaults import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('yaba2.views',
    url(r'^$', 'index', name='index'),
)

urlpatterns += staticfiles_urlpatterns()
