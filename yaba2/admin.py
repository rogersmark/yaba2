from django.contrib import admin

from django_markdown.admin import MarkdownModelAdmin

from . import models

class StoryAdmin(MarkdownModelAdmin):
    ''' Admin adjustments for models.Story '''
    list_display = ('title', 'author', 'status', 'created', 'modified')
    search_fields = ('title', 'post')
    list_filter = ('status', 'author', 'created', 'modified')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Link)
admin.site.register(models.Story, StoryAdmin)
