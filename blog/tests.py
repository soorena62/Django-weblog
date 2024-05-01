from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from .models import Post

# Create your tests here:


class BlogPostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='majid-n')
        cls.post_1 = Post.objects.create(
            title='Django',
            body='Django is a free and open-source, Python-based web framework that runs on a web server.',
            status='pub',  # Published
            author=cls.user,
        )
        cls.post_2 = Post.objects.create(
            title='DataScience And Python',
            body='Python is a programming language widely used by Data Scientists.',
            status='drf',  # Draft
            author=cls.user,
        )

    def test_post_title_should_print(self):
        post = self.post_1
        self.assertEqual(str(post), post.title)

    def test_post_detail(self):
        self.assertEqual(self.post_1.title, 'Django')
        self.assertEqual(self.post_1.body, 'Django is a free and open-source,'
                                           ' Python-based web framework that runs on a web server.')

    def test_post_list_urls(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_posts_list_urls_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_posts_title_on_posts_list(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post_1.title)

    def test_post_detail_url(self):
        response = self.client.get(f'/blog/{self.post_1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_detail_view_urls_by_name(self):
        response = self.client.get(reverse('post_detail_view', args=[self.post_1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_details_on_detail_page(self):
        response = self.client.get(reverse('post_detail_view', args=[self.post_1.id]))
        self.assertContains(response, self.post_1.title)
        self.assertContains(response, self.post_1.body)

    def test_status_post_id_not_exist(self):
        response = self.client.get(reverse('post_detail_view', args=[1000]))
        self.assertEqual(response.status_code, 404)

    def test_status_post_draft_not_show_on_post_lists(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post_1.title)
        self.assertNotContains(response, self.post_2.title)

    def test_create_post_view(self):
        response = self.client.post(reverse('create_post'), {
            'title': 'DataScience And Python',
            'body': 'Python is a programming language widely used by Data Scientists.',
            'status': 'pub',
            'author': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'DataScience And Python')
        self.assertEqual(Post.objects.last().body, 'Python is a programming language widely used by Data Scientists.')

    def test_update_post_view(self):
        response = self.client.post(reverse('update_post', args=[self.post_2.id]), {
            'title': 'test title updated',
            'body': 'test body updated',
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Post.objects.last().title, 'DataScience And Python')
        self.assertEqual(Post.objects.last().body, 'Python is a programming language widely used by Data Scientists.')

    def test_delete_post_view(self):
        response = self.client.post(reverse('delete_post', args=[self.post_2.id]),)
        self.assertEqual(response.status_code, 302)

