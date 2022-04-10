from django.contrib import admin
from .models import *
# Register your models here.


class ItemCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(ItemCategory,ItemCategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','offerprice','price','available','details','stock']
    list_editable = ['offerprice','available','details','stock']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Products,ProductAdmin)