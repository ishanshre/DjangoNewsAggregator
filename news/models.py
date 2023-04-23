from django.db import models

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    published_date = models.DateTimeField(null=True, blank=True)
    link = models.URLField()
    image = models.URLField(null=True, blank=True)
    source_title = models.CharField(max_length=255)
    guid = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class FeedSource(models.Model):
    link = models.URLField()
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title