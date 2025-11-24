# tasks/admin.py
from django.contrib import admin
from .models import Task, TaskMedia

# დარეგისტრირება:
admin.site.register(Task)
admin.site.register(TaskMedia)