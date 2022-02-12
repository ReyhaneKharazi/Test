from django.shortcuts import render,get_object_or_404
from blog.models import Post
from datetime import datetime
from django.db.models import F

# Create your views here.
def home(request):
    return render(request,'index.html')

def blog_gird(request):
    posts = Post.objects.filter(published_date__lte=datetime.now())
    context = {'posts': posts}
    return render(request,'blog-grid.html',context)


def blog_single(request):
    # post = get_object_or_404(Post, pk=pid)
    
    # context = {'post': post}
    return render(request,'blog-single.html')
