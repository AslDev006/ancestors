from django.contrib import admin
from .models import *
@admin.register(Person)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'date_of_birth']
    list_filter = ['create_time']
    date_hierarchy = 'create_time'
    search_fields = ['first_name', 'second_name', 'third_name']
    ordering = ["create_time"]

admin.site.register([Roles, Family, Family_Media])