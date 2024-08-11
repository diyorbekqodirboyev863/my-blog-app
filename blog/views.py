from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages as msg
from . import models


# Home.
def home(request):
    '''Home.'''
    posts = models.Post.objects.all() # Get all post.
    post = models.Post.objects.filter(is_featured=True).last() # Get the header post.
    return render(request=request, template_name='home.html', context={'posts': posts, 'post': post})

# About.
def about(request):
    '''About.'''
    return render(request=request, template_name='about.html', context={})

# Blog.
def blog(request):
    '''Blog.'''
    posts = models.Post.objects.filter(is_featured=False, is_blog_featured=False) # Get all posts.
    post = models.Post.objects.filter(is_blog_featured=True).last() # Get the header post of the blog.
    categories = models.Category.objects.all() # Get all categories.
    return render(request=request, template_name='blog.html', context={'posts': posts, 'post': post ,'categories': categories})

# Contact.
def contact(request):
    '''Contact.'''
    return render(request=request, template_name='contact.html', context={})