#from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Student, Tel, Department

admin.site.register(Student)
admin.site.register(Tel)
admin.site.register(Department)
