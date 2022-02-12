from email.policy import default
from pickle import FALSE
from django.db import models

# Create your models here.
class Post(models.Model):
    category = models.CharField(max_length=255)
    picture = models.ImageField(max_length=255,default='statics/assets/img/post-1.jpg')
    title = models.CharField(max_length=255)
    about_title = models.CharField(max_length=255)
    published_date = models.DateField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=255)
    content = models.TextField()
    quote_content = models.TextField()
    quote_author = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    counted_views = models.PositiveIntegerField(default=0)



    def __str__(self):
        return self.title+str(self.id)
