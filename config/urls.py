from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('api-auth/',include('dj_rest_auth.urls')),
    path('',include('book.urls')),
    path('admin/', admin.site.urls),
]
