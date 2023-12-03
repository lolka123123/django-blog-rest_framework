from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.User)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']