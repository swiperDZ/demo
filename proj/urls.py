"""proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from App1 import user_apis

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^app1/', include('App1.urls', namespace='app1')),
    url(r'^app2/', include('App2.urls', namespace='app2')),
    url(r'^numberver/', user_apis.number_verification, name='numberver'),
    url(r'^vcodever/', user_apis.v_code_verification, name='vcodever'),
]
