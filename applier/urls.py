from django.contrib import admin
from django.urls import include, re_path
from django.shortcuts import redirect
from applier import views

urlpatterns = [
    re_path('^(?P<short_code>[a-zA-Z0-9]{6})/', views.applier)
]
