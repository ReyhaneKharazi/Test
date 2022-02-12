from asyncio.proactor_events import _ProactorBasePipeTransport
from django import template
from blog.models import Post
register = template.Library()

@register.filter(name="shorter")
def current_time(content):
    return content[:10]

@register.inclusion_tag('latest_posts.html')
def latest_posts():
    posts = Post.objects.filter(status=True).order_by('-published_date')
    return {'posts':posts[:6]}