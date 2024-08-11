from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# CustomUser.
class CustomUser(AbstractUser):
    # Additional fields.
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    # profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    # website = models.URLField(null=True, blank=True)
    # facebook_url = models.URLField(null=True, blank=True)
    # twitter_url = models.URLField(null=True, blank=True)
    # instagram_url = models.URLField(null=True, blank=True)
    # github_url = models.URLField(null=True, blank=True)
    # linkedin_url = models.URLField(null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # is_verified = models.BooleanField(default=False)
    # is_admin = models.BooleanField(default=False)

