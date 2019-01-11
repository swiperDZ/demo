from django.conf.urls import url

from App1 import views

urlpatterns = [
    url(r'^hello/', views.HelloView.as_view())
]