from django.contrib import admin
from .models import CommentModel, Profile
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(CommentModel)
admin.site.register(Profile)
