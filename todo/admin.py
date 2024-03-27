from django.contrib import admin

from todo.models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['task', 'is_completed', 'updated_at']

# Register your models here.
admin.site.register(Task, TaskAdmin)