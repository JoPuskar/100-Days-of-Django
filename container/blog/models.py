from django.utils import timezone

from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField(max_length=1000)
    photo = models.ImageField(null=True, blank=True, upload_to="blog/photos")
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
