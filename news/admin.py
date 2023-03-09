from django.contrib import admin
from .models import *


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']


@admin.register(NewsModel)
class NewsModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_descriptions', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']
