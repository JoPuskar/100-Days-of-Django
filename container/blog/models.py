from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models

from tinymce.models import HTMLField

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField(max_length=1000)
    author = models.ForeignKey(User, null=True, blank=True, related_name='blog', on_delete=models.SET_NULL)
    photo = models.ImageField(null=True, blank=True, upload_to="blog/photos")
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

    def __str__(self):
        return self.blog.title

    class Meta:
        unique_together = ('blog', 'user',)


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    comment = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment

