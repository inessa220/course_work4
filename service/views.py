from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from service.models import Client, Message, Mailing


class HomeView(TemplateView):
    template_name = "home.html"
    context_object_name = "home"


class ClientListView(ListView):
    model = Client
    template_name = "client_list.html"
    context_object_name = "clients"


class ClientDetailView(DetailView):
    model = Client
    template_name = "client_detail.html"


class ClientCreateView(CreateView):
    model = Client
    fields = ("email", "name", "comment")
    template_name = "client_form.html"

    def get_success_url(self):
        return reverse_lazy("service:client_list")


class ClientUpdateView(UpdateView):
    model = Client
    fields = ("email", "name", "comment")
    template_name = "client_form.html"

    def get_success_url(self):
        return reverse_lazy("service:client_list")


class ClientDeleteView(DeleteView):
    model = Client
    template_name = "client_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("service:client_list")


class MessageListView(ListView):
    model = Message
    template_name = "message_list.html"
    context_object_name = "messages"


class MessageDetailView(DetailView):
    model = Message
    template_name = "message_detail.html"


class MessageCreateView(CreateView):
    model = Message
    fields = ("topic", "text")
    template_name = "message_form.html"

    def get_success_url(self):
        return reverse_lazy("service:messages_list")


class MessageUpdateView(UpdateView):
    model = Message
    fields = ("topic", "text")
    template_name = "message_form.html"

    def get_success_url(self):
        return reverse_lazy("service:messages_list")


class MessageDeleteView(DeleteView):
    model = Message
    template_name = "message_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("service:messages_list")


class MailingListView(ListView):
    model = Mailing
    template_name = "mailing_list.html"
    context_object_name = "mailings"

class MailingDetailView(DetailView):
    model = Mailing
    template_name = "mailing_detail.html"


class MailingCreateView(CreateView):
    model = Mailing
    fields = ("start_send", "stop_send", "status", "message", "clients")
    template_name = "mailing_form.html"

    def get_success_url(self):
        return reverse_lazy("service:mailing_list")


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ("start_send", "stop_send", "status", "message", "clients")
    template_name = "mailing_form.html"

    def get_success_url(self):
        return reverse_lazy("service:mailing_list")


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = "mailing_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy("service:mailing_list")

