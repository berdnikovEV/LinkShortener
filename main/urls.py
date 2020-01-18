from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('register.urls')),
    path('sign_in/', include('sign_in.urls')),
    path('shorten/', include('shorten.urls')),
    path('tags/', include('tag_search.urls')),
    path('', include('applier.urls'))
]
