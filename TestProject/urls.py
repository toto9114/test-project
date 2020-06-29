"""TestProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from oauth2_provider.models import Application

import api.urls


def make_test_application():
    print('make test application')
    app, create = Application.objects.get_or_create(
        client_id='T3u5jsjokORO9UCMeFG6mxbOuLungS5iKIFi1tXP',
        client_secret='NUySERaNpiiBz6rAQ3AlJeL49SO0QrlK2ja5OmhyUUiCnTbND2wZEUwisgp0OdlmTD6cPVm08ywSkWatFBhkxp29LZKbUbmgIT1q1mXLODyRZTHrk33PRIkDhlcBnduh',
        client_type='confidential',
        authorization_grant_type='password',
        name='test-project'
    )


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api.urls.urlpatterns)),
]

make_test_application()
