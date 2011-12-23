''' yaba2 models '''
from django.db import models

from taggit.managers import TaggableManager

class YabaBaseModel(models.Model):
    ''' Base model, provides standard fields that all yaba2 models will need
    '''

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Link(YabaBaseModel):
    ''' Links to other sites to put in the sidebar and what not '''

    label = models.CharField(max_length=100)
    url = models.CharField(max_length=256)

    def __unicode__(self):
        return u'%s' % self.label

class StoryManager(models.Manager):
    ''' Helper functions for the Story model '''

    @property
    def published_stories(self):
        return self.filter(status=self.model.PUBLISHED)

    @property
    def drafts(self):
        return self.filter(status=self.model.DRAFT)

    @property
    def archived_stories(self):
        return self.filter(status=self.model.ARCHIVED)

class Story(YabaBaseModel):
    ''' Story model to hold blog posts and articles '''

    DRAFT = 1
    PUBLISHED = 2
    ARCHIVED = 3

    STATUS_CHOICES = (
        (PUBLISHED, 'Published'),
        (DRAFT, 'Draft'),
        (ARCHIVED, 'Archived')
    )

    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    post = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    enable_comments = models.BooleanField()
    tags = TaggableManager()

    objects = StoryManager()

    def __unicode__(self):
        return u'%s by %s' % (self.title, self.author.username)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'stories'
