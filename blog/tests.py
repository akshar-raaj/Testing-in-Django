from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.staticfiles import finders
from django.contrib.staticfiles.storage import staticfiles_storage

from blog.models import BlogEntry


class BlogEntriesTest(TestCase):

    def setUp(self):
        self.c = Client()
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")

    def test_entries_access(self):
        response = self.c.get(reverse('entries'))
        self.assertEqual(response.status_code, 200)

    def test_entries_template_context(self):
        #create few blog entries
        BlogEntry.objects.create(title='Test', text='Test', user=self.user)
        BlogEntry.objects.create(title='Test', text='Test', user=self.user)

        response = self.c.get(reverse('entries'))
        #assert that context contains as many entries as you expect
        self.assertEqual(len(response.context['entries']), 2)

    def test_entry_create(self):
        response = self.c.get(reverse('entry_create'))
        self.assertEqual(response.status_code, 302)

        self.c.login(username='test', password='test')
        response = self.c.get(reverse('entry_create'))
        self.assertEqual(response.status_code, 200)

    def test_invalid_entry_create(self):
        self.c.login(username='test', password='test')
        data = {'text': 'Test text'}
        response = self.c.post(reverse('entry_create'), data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, "form", "title", "This field is required.")

    def test_valid_entry_create(self):
        self.c.login(username='test', password='test')
        data = {'text': 'Test text', 'title': 'Test title'}
        data['user'] = self.user.id
        self.assertEqual(BlogEntry.objects.count(), 0)
        response = self.c.post(reverse('entry_create'), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BlogEntry.objects.count(), 1)

    def test_entry_custom_managers(self):
        BlogEntry.objects.create(title='Test', text='Test', user=self.user, is_published=False)
        BlogEntry.objects.create(title='Test', text='Test', user=self.user)
        self.assertEqual(BlogEntry.objects.count(), 2)
        self.assertEqual(BlogEntry.published.count(), 1)

    def test_entries_page(self):
        for i in range(15):
            BlogEntry.objects.create(title="title", text="text", user=self.user, is_published=True)

        #access first page
        response = self.c.get(reverse("entries_page", args=[1,]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['entries']), 10)

        #access second page
        response = self.c.get(reverse("entries_page", args=[2,]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['entries']), 5)

        #access third page
        response = self.c.get(reverse("entries_page", args=[3,]))
        self.assertEqual(response.status_code, 404)

    def test_images(self):
        abs_path = finders.find('default.jpg')
        self.assertTrue(staticfiles_storage.exists(abs_path))
