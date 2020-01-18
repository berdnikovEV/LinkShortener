from django.contrib import admin
from django.urls import include, re_path
from django.shortcuts import redirect
from tag_search import views

urlpatterns = [
    re_path('^(?P<tag>[a-zA-Z0-9]*)/', views.search)
]
