from django.contrib import admin
from .models import Student
# Register your models here.
@admin.register(Student)
class stu_admin(admin.ModelAdmin):
    list_display = ['name','age','city']