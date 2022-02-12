from re import search
from django.contrib import admin
from blog.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','category','author','created_date','published_date','updated_date',)
    list_filter = ('status','author',)
    search_fields = ('title','author','created_date',)
    date_hierarchy = ('created_date')

admin.site.register(Post,PostAdmin)