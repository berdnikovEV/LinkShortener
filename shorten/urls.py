from django.urls import path
from shorten import views

urlpatterns = [
    path('', views.shorten),
    path('success/', views.success)
]
