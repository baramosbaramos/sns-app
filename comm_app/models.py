from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class CommentModel(models.Model):
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True, default=False)
    image = models.ImageField(null=True, blank=True, upload_to='')
    read = models.IntegerField(null=True, blank=True, default=1)
    time = models.DateTimeField(default=timezone.now)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, upload_to='', default='avatar1.png')
    favorite_words = models.CharField(max_length=50, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()