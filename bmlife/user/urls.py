from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'social/(?P<backend>[^/]+)/$', views.exchange_token)
]