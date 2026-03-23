from django.contrib import admin

# Register your models here.
from .models import Project, Task, Client
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


admin.site.register(CustomUser,UserAdmin)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Client)

