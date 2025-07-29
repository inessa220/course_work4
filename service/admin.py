from django.contrib import admin
from .models import Client, Message, Mailing

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'name', 'comment')
    search_fields = ('email', 'name')
    list_filter = ('comment',)

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'topic', 'text')
    search_fields = ('topic', 'text')
    list_filter = ('topic',)

@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'start_send', 'stop_send', 'status')
    search_fields = ('status', 'message')
    list_filter = ('status',)




