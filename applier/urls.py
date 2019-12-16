from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
from applier import views

urlpatterns = [
    path('<str:short_code>', views.applier)
]
