from django.contrib import admin

# Register your models here.
from my_shop.models import Products, Categories

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "description", "price", "image", "category", "created"]
    search_fields = ["name", "id"]
    fields = ["name", "description", "price", "image", "category", "created"]
    readonly_fields = ["created"]


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]

admin.site.register(Products, ProductAdmin)
admin.site.register(Categories, CategoriesAdmin)