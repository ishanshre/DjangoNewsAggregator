from django.contrib import admin

from news.models import Content, FeedSource
# Register your models here.

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['title','published_date']

admin.site.register(FeedSource)