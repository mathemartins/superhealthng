from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
# Dont Repeat Yourself = DRY

from blog.models import BlogPost


def home_page(request):
    qs = BlogPost.objects.all()[:5]
    context = {"title": "Welcome to SuperHealthng", 'blog_list': qs}
    return render(request, "home.html", context)


def about_page(request):
    return render(request, "about.html", {"title": "About"})
