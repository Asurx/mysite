"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.urls import path
from .views import blog_list, blog_list_with_type, blog_detail

urlpatterns = [
    path('', blog_list, name="blog_list"),
    path('id/<int:blog_pk>', blog_detail, name="blog_detail"),
    path('type/<int:blog_type_pk>', blog_list_with_type, name="blog_list_with_type"),
]
