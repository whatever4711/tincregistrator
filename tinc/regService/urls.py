from django.conf.urls import url

from . import views
from .views import ConfigView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^config', ConfigView.as_view(), name='config'),
]
