from django.contrib import admin
from .models import Room, Message

# Register your models here.
admin.site.register(Room)
class AdminMessage(admin.ModelAdmin):
    list_display = ['content','room']
admin.site.register(Message,AdminMessage)