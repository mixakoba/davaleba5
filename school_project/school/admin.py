from django.contrib import admin
from .models import Teacher,Student,Class

admin.site.register(Teacher)
admin.site.register(Class)
admin.site.register(Student)