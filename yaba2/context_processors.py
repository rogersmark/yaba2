''' Context Processors for yaba2 '''

from yaba2 import models

def sidebar_links(request):
    ''' Grabs our link objects and throws them in the context '''
    return {'link_groups': models.LinkGroup.objects.all()}
