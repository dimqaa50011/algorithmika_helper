from django.contrib import admin

from .models import TgUser, MiniCours, Student


@admin.register(TgUser)
class TgUserAdmin(admin.ModelAdmin):
    list_display = ('tg_id', 'first_name', 'tg_username')
    list_display_links = ('tg_id', 'first_name', 'tg_username')


@admin.register(MiniCours)
class MiniCoursAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'start_time')
    list_display_links = ('title',)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_presence')
    list_display_links = ('first_name', 'last_name')
