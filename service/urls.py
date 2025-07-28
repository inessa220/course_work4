from django.urls import path, include
from service.apps import ServiceConfig

app_name = ServiceConfig.name

urlpatterns = [
    path(
        "",
    )
]
