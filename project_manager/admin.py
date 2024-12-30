from django.contrib import admin

# Register your models here.
from .models import Project, Member, Task, Comment

admin.site.register(Project)
admin.site.register(Member)
admin.site.register(Task)
admin.site.register(Comment)
