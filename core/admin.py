from django.contrib import admin
from .models import Caddy

@admin.register(Caddy)
class CaddyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "level", "phone", "availability")
    search_fields = ("name", "phone")
    list_filter = ("level",)
