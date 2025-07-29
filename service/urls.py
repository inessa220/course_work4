from django.urls import path, include
from service.apps import ServiceConfig
from service.views import home

app_name = ServiceConfig.name

urlpatterns = [path("", home, name="home")]
