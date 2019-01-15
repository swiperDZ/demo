from django.conf.urls import url

from App1 import views

urlpatterns = [
    url(r'^user/$', views.UserMessageView.as_view(), name= 'user'),
    url(r'^useramend/(?P<id>\d+)/', views.UserAmendView.as_view(), name= 'useramend')
]