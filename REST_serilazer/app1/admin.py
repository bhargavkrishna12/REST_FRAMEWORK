from django.contrib import admin

# Register your models here.
from.models import Movies

@admin.register(Movies)
class Admin(admin.ModelAdmin):
    list_display = ['name','rate','city']