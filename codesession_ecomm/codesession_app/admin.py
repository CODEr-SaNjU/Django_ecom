from django.contrib import admin

from .models import ProductType, Product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['Product_Name']
    list_display = ('Product_Name', 'Product_Type', 'Product_Price')


admin.site.register(ProductType)
admin.site.register(Product, ProductAdmin)
