from django.urls import path, include
from service.apps import ServiceConfig
from service.views import (
    HomeView,
    ClientListView,
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView,
    MessageListView,
    MessageCreateView,
    MessageUpdateView,
    MessageDeleteView, MailingListView, MailingCreateView, MailingUpdateView, MailingDeleteView, ClientDetailView,
    MessageDetailView,
)

app_name = ServiceConfig.name

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    # clients
    path("clients/", ClientListView.as_view(), name="client_list"),
    path("clients/create/", ClientCreateView.as_view(), name="client_create"),
    path("clients/<int:pk>/update/", ClientUpdateView.as_view(), name="client_update"),
    path("clients/<int:pk>/delete/", ClientDeleteView.as_view(), name="client_delete"),
    path("clients/<int:pk>/", ClientDetailView.as_view(), name="client_detail"),
    # message
    path("messages/", MessageListView.as_view(), name="messages_list"),
    path("messages/create/", MessageCreateView.as_view(), name="messages_create"),
    path("messages/<int:pk>/update/", MessageUpdateView.as_view(), name="messages_update"),
    path("messages/<int:pk>/delete/", MessageDeleteView.as_view(), name="messages_delete"),
    path("messages/<int:pk>/", MessageDetailView.as_view(), name="messages_detail"),
    # mailing
    path("mailing/", MailingListView.as_view(), name="mailing_list"),
    path("mailing/create/", MailingCreateView.as_view(), name="mailing_create"),
    path("mailing/<int:pk>/update/", MailingUpdateView.as_view(), name="mailing_update"),
    path("mailing/<int:pk>/delete/", MailingDeleteView.as_view(), name="mailing_delete"),
]
