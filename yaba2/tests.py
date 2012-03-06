''' Tests for assorted yaba2 functionality '''
from django.test import TestCase
from django.core.urlresolvers import reverse


class TestYaba2Views(TestCase):

    fixtures = ['test_data.json', 'test_tags.json']

    def setUp(self):
        super(TestYaba2Views, self).setUp()

    def tearDown(self):
        super(TestYaba2Views, self).tearDown()

    def test_main_index(self):
        ''' Tests the main index view of yaba2 '''
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['story_list']), 3)
        self.assertEqual(len(response.context['links']), 3)

    def test_story_detail(self):
        ''' Tests the detail story view '''
        response = self.client.get(reverse('story-detail', args=['story-1']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['links']), 3)

    def test_list_tag(self):
        ''' Tests the tag list view '''
        response = self.client.get(reverse('tag-stories',
            kwargs={'tag_name': 'cats'}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['story_list']), 1)
        self.assertEqual(len(response.context['links']), 3)
