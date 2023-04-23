"""
Creating custom command for parsing the feeds
"""
import feedparser
from dateutil import parser
from datetime import datetime

from news.models import FeedSource, Content

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        """
        Creating a parser that parses the feed from RSS sources
        """
        # getting all the RSS sources from the database
        sources = FeedSource.objects.all() 

        # iterating the feed source
        for source in sources:
            # parsing the feed from a source link address
            feed = feedparser.parse(source.link)
            source_title = ''
            source_image = ''
            if 'title' in feed.channel:
                source_title = feed.channel.title
            if 'image' in feed.channel:
                source_image = feed.channel.image['href']
            
            for item in feed.entries:
                if not Content.objects.filter(guid=item.guid).exists():
                    description = 'No Description'
                    if 'description' in item:
                        description = item.description
                    if 'published' in item:
                        content = Content.objects.create(
                        title=item.title,
                        description=description,
                        published_date=parser.parse(item.published),
                        link=item.link,
                        image=source_image,
                        source_title=source_title,
                        guid=item.guid,
                        )
                    else:
                        content = Content.objects.create(
                        title=item.title,
                        description=description,
                        link=item.link,
                        image=source_image,
                        source_title=source_title,
                        guid=item.guid,
                        )
                    content.save()
