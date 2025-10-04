from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MessageLog

@admin.register(MessageLog)
class MessageLogAdmin(admin.ModelAdmin):
    list_display = ("message_preview", "created_at")
    readonly_fields = ("message", "predictions", "created_at")

    def message_preview(self, obj):
        return obj.message[:50]
    message_preview.short_description = "Message"
