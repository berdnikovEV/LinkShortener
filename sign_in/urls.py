from django.urls import path
from sign_in import views

urlpatterns = [
    path('', views.sign_in),
    path('success/', views.success)
]
