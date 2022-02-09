from django.contrib import admin

# Register your models here.
from .models import student_model

admin.site.register(student_model)