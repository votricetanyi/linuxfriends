from django.contrib import admin

# Register your models here.

from .models import Teacher, TelTeacher

admin.site.register(Teacher)
admin.site.register(TelTeacher)
