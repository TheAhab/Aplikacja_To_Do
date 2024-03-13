from django.contrib import admin
from .models import Task, Date, Tag
# Register your models here.
admin.site.register(Task)
admin.site.register(Date)
admin.site.register(Tag)