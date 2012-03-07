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

class LinkGroup(YabaBaseModel):
    ''' Groupings for Links '''

    title = models.CharField(max_length=64)
    sort_order = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.title

    class Meta:
        ordering = ['sort_order']

class Link(YabaBaseModel):
    ''' Links to other sites to put in the sidebar and what not '''

    label = models.CharField(max_length=100)
    url = models.CharField(max_length=256)
    group = models.ForeignKey('LinkGroup')
    sort_order = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.label

    class Meta:
        ordering = ['sort_order']

class StoryManager(models.Manager):
    ''' Helper functions for the Story model '''

    @property
    def published_stories(self):
        ''' Returns queryset of published stories '''
        return self.filter(
                status=self.model.PUBLISHED,
                story_type=self.model.NEWS
        )

    @property
    def drafts(self):
        ''' Returns queryset of stories in draft status '''
        return self.filter(
                status=self.model.DRAFT,
                story_type=self.model.NEWS
        )

    @property
    def archived_stories(self):
        ''' Returns queryset of archived stories '''
        return self.filter(
                status=self.model.ARCHIVED,
                story_type=self.model.NEWS
        )

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

    NEWS = 1
    PAGE = 2

    STORY_TYPES = (
        (NEWS, 'News'),
        (PAGE, 'Page'),
    )

    author = models.ForeignKey('auth.user')
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    post = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    story_type = models.IntegerField(choices=STORY_TYPES, default=1)
    enable_comments = models.BooleanField()
    tags = TaggableManager()

    objects = StoryManager()

    @models.permalink
    def get_absolute_url(self):
        return ('story-detail', (), {'slug': self.slug})

    def __unicode__(self):
        return u'%s by %s' % (self.title, self.author.username)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'stories'
