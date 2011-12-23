''' yaba2 models '''
from django.db import models

class YabaBase(models.Model):
    ''' Base model, provides standard fields that all yaba2 models will need
    '''

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Link(models.Model):
    ''' Links to other sites to put in the sidebar and what not '''

    label = models.CharField(max_length=100)
    url = models.CharField(max_length=256)

    def __unicode__(self):
        return u'%s' % self.label

