from unicodedata import name
from django.urls import path,include
from blog.views import *

app_name='blog'

urlpatterns = [
    path('',home,name="index"),
    path('blog-grid',blog_gird,name="blog-grid"),
    path('blog-single',blog_single,name="blog-single"),
    path('blog-single/<int:pid>',blog_single,name="blog-single"),
]
