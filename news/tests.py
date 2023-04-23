from django.test import TestCase
from django.utils import timezone
from news.models import Content
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
        