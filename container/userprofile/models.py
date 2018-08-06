from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(blank=True, upload_to='users/profile_pic/')
    bio = models.TextField(max_length=200, blank=True)
    address = models.CharField(max_length=120, blank=True)

    def __str__(self):
        if self.user.first_name and self.user.last_name:
            full_name = self.user.first_name +" "+ self.user.last_name
            return full_name
        return self.user.username

    @property
    def get_fullname(self):
        return self.user.first_name + " "+ self.user.last_name


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):
    instance.profile.save()
