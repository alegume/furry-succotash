'''
    mysite URL Configuration
'''

from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('blog.urls')),
    path('polls/', include('polls.urls'))
]
