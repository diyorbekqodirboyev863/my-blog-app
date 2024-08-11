from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        self.slug = slugify(self.name.lower())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

# Post.
class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_blog_header = models.BooleanField(default=False)
    is_header = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.title = self.title.title()
        self.slug = slugify(self.title.lower())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
