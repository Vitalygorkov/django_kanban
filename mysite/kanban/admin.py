from django.contrib import admin
from .models import Category, Task, Status

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Status)