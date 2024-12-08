from django.contrib import admin

from .models import Category, Product, Address


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'price')
    list_filter = ('category',)
    search_fields = ('title', 'description')


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'country', 'INN', 'address')
