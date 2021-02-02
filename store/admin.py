from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.oder import Oder

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category', 'price', 'image']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Oder)
