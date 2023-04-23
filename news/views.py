from django.shortcuts import render
from django.views.generic import ListView

from news.models import Content

class IndexPageView(ListView):
    model = Content
    context_object_name = "contents"
    template_name = "index.html"
