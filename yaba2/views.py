from django.shortcuts import render
from django.views.generic import ListView

from yaba2 import models

def index(request):

    return render(request, 'index.html', {})

class StoryListView(ListView):
    ''' Generic ListView to handle stories properly '''

    paginate = True
    paginate_by = 5
    context_object_name = 'story_list'
    template_name = 'yaba2/story_list.html'

    def get_queryset(self, **kwargs):
        ''' If a tag is passed in, filter by that '''
        if self.kwargs.get('tag_name'):
            return models.Story.objects.published_stories.filter(
                tags__name=self.kwargs['tag_name'])
        return models.Story.objects.published_stories
