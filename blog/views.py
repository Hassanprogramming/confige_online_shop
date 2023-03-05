from django.views import View
from django.shortcuts import render
from .models import *
# Create your views here.


class blogView(View):
    def get(self, request):
        admin = Admin.objects.all()
        news = New.objects.all()
        blogs = Blogs.objects.all()
        return render(request, "blog/blog.html",{'blogs': blogs, 'news':news, 'admin':admin})

