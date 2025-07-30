from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView, DetailView
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
        return reverse_lazy('service:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    fields = ("email", "name", "comment")
    template_name = "client_form.html"

    def get_success_url(self):
        return reverse_lazy('service:client_list')


class ClientDeleteView(DeleteView):
    model = Client
    template_name = "client_confirm_delete.html"

    def get_success_url(self):
        return reverse_lazy('service:client_list')


class MessageListView(ListView):
    model = Message
    template_name = "message_list.html"


class MessageCreateView(CreateView):
    model = Message
    field = ("topic", "text")
    template_name = "message_form.html"
    success_url = reverse_lazy("message_list.html")


class MessageUpdateView(UpdateView):
    model = Message
    template_name = "message_form.html"
    success_url = reverse_lazy("message_list.html")


class MessageDeleteView(DeleteView):
    model = Message
    template_name = "message_confirm_delete"
    success_url = reverse_lazy("message_list.html")


class MailingListView(ListView):
    model = Mailing
    template_name = "mailing_list.html"


class MailingCreateView(CreateView):
    model = Mailing
    field = ("topic", "text")
    template_name = "mailing_form.html"
    success_url = reverse_lazy("mailing_list.html")


class MailingUpdateView(UpdateView):
    model = Mailing
    template_name = "mailing_form.html"
    success_url = reverse_lazy("mailing_list.html")


class MailingDeleteView(DeleteView):
    model = Mailing
    template_name = "mailing_confirm_delete"
    success_url = reverse_lazy("mailing_list.html")
