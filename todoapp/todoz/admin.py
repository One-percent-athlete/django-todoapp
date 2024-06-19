from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Category, Priority, User, Todo

admin.site.unregister(Group)

admin.site.register(Category)

admin.site.register(Priority)

@admin.register(Todo)
class TodosAdmin(admin.ModelAdmin):
    list_display = ('user', 'task_name','category', 'task_body','created_at', 'priority','deadline')
    search_fields = ('user', 'task_name')
