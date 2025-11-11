# INF 601 - Advanced Python
# Illia Ivanov
# Mini Project 4

from django.contrib import admin
from .models import DailyEntry, DailyTask


class DailyTaskInline(admin.TabularInline):
    """Inline admin for tasks within a daily entry"""
    model = DailyTask
    extra = 1
    fields = ['title', 'completed', 'priority']


@admin.register(DailyEntry)
class DailyEntryAdmin(admin.ModelAdmin):
    """Admin configuration for DailyEntry model """
    list_display = ['date', 'user', 'title', 'mood', 'created_at']
    list_filter = ['mood', 'date', 'user']
    search_fields = ['title', 'content']
    date_hierarchy = 'date'
    inlines = [DailyTaskInline]

    fieldsets = (
        ('Entry Information', {
            'fields': ('user', 'date', 'title', 'mood')
        }),
        ('Content', {
            'fields': ('content',)
        }),
    )


@admin.register(DailyTask)
class DailyTaskAdmin(admin.ModelAdmin):
    """Admin configuration for DailyTask modell """
    list_display = ['title', 'daily_entry', 'priority', 'completed', 'created_at']
    list_filter = ['priority', 'completed', 'created_at']
    search_fields = ['title']
    list_editable = ['completed', 'priority']