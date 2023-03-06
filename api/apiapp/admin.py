from django.contrib import admin

from .models import TgUser


@admin.register(TgUser)
class TgUserAdmin(admin.ModelAdmin):
    list_display = ('tg_id', 'first_name', 'tg_username')
    list_display_links = ('tg_id', 'first_name', 'tg_username')
