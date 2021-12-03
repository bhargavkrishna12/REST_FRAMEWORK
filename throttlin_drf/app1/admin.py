from django.contrib import admin

# Register your models here.
from .models import Movies
@admin.register(Movies)
class admin_m(admin.ModelAdmin):
    list_display = ['movie_id','movie_name','location']
