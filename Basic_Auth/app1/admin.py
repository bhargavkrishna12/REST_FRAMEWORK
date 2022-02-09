from django.contrib import admin

# Register your models here.
from app1.models import praveen


@admin.register(praveen)
class student_adm(admin.ModelAdmin):
    list_display = ('name','roll_num', 'age')

