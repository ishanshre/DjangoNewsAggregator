from django.test import TestCase
from django.utils import timezone
from news.models import Content
from django.urls import reverse
# Create your tests here.

class NewsModelTest(TestCase):
    def setUp(self):
        self.content = Content.objects.create(
            title="Learn Django",
            description="Learning the latest version of django",
            published_date=timezone.now(),
            link="https://myawesomeshow.com",
            image="https://image.myawesomeshow.com",
        )

    def test_content_content(self):
        self.assertEqual(self.content.title, "Learn Django")
        self.assertEqual(self.content.description, "Learning the latest version of django")
    
    def test_index_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_index_page_correct_template_use(self):
        response = self.client.get(reverse("news:index"))
        self.assertTemplateUsed(response, "index.html")
    
    def test_index_list_contains(self):
        response = self.client.get(reverse("news:index"))
        self.assertContains(response, "Learn Django")