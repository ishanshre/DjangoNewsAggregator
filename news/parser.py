import feedparser

from news.models import Content, FeedSource

sources = FeedSource.objects.all()
for source in sources:
    feed = feedparser.parse(source.link)
    title = feed.channel.title
    image = feed.channel.image["href"]
    for item in feed.entries:
        if not Content.objects.filter(guid=item.guid).exists():
            content = Content.objects.create(
                title=item.title,
                description=item.description,
                published_date=item.published_parsed,
                link=item.link,
                image=image,
                source_title = title,
                guid=item.guid
            )
            content.save()