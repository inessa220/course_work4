from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from django.views.decorators.cache import cache_page
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from service.models import Client, Message, Mailing


@cache_page(60 * 15)
@login_required
def home(request):
    total_mailings = Mailing.objects.count()
    active_mailings = Mailing.objects.filter(status="running").count()
    unique_clients = Client.objects.values("email").distinct().count()
    context = {
        "total_mailings": total_mailings,
        "active_mailings": active_mailings,
        "unique_clients": unique_clients,
    }
    return render(request, "home.html", context)


class HomeView(TemplateView):
    template_name = "home.html"
    context_object_name = "home"


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = "client_list.html"
    context_object_name = "clients"

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = "client_detail.html"

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    fields = ("email", "name", "comment")
    template_name = "client_form.html"

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy("service:client_list")


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ("email", "name", "comment")
    template_name = "client_form.html"

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy("service:client_list")


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    template_name = "client_confirm_delete.html"

    def get_queryset(self):
        return Client.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy("service:client_list")


class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    template_name = "message_list.html"
    context_object_name = "messages"

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)

class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    template_name = "message_detail.html"

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ("topic", "text")
    template_name = "message_form.html"

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy("service:messages_list")


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    fields = ("topic", "text")
    template_name = "message_form.html"

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy("service:messages_list")


class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    template_name = "message_confirm_delete.html"

    def get_queryset(self):
        return Message.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy("service:messages_list")


class MailingListView(LoginRequiredMixin, ListView):
    model = Mailing
    template_name = "mailing_list.html"
    context_object_name = "mailings"

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)


class MailingDetailView(LoginRequiredMixin, DetailView):
    model = Mailing
    template_name = "mailing_detail.html"

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)


class MailingCreateView(LoginRequiredMixin, CreateView):
    model = Mailing
    fields = ("start_send", "stop_send", "status", "message", "clients")
    template_name = "mailing_form.html"

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy("service:mailing_list")


class MailingUpdateView(LoginRequiredMixin, UpdateView):
    model = Mailing
    fields = ("start_send", "stop_send", "status", "message", "clients")
    template_name = "mailing_form.html"

    def get_success_url(self):
        return reverse_lazy("service:mailing_list")

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)


class MailingDeleteView(LoginRequiredMixin, DeleteView):
    model = Mailing
    template_name = "mailing_confirm_delete.html"

    def get_queryset(self):
        return Mailing.objects.filter(owner=self.request.user)

    def get_success_url(self):
        return reverse_lazy("service:mailing_list")

def main(request: HttpRequest):
    user = request.user
    context = {"total_mailings": 0, "active_mailings": 0, "unique_clients": 0}
    if user.is_authenticated:
        context["total_mailings"] = Message.objects.filter(owner=user.id).count()
        context["active_mailings"] = Mailing.objects.filter(owner=user.id).count()
        context["unique_clients"] = Client.objects.filter(owner=user.id).count()
    else:
        context["total_mailings"] = Message.objects.all().count()
        context["active_mailings"] = Mailing.objects.all().count()
        context["unique_clients"] = Client.objects.all().count()
    return render(request, template_name="main.html", context=context)
