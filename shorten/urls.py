from django.urls import path
from shorten import views

urlpatterns = [
    path('', views.shorten, name='shorten'),
    path('success/', views.success, name='shorten-success')
]
