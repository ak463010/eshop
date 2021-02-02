from django.db import models
from django.db.models.deletion import CASCADE
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=80)
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=255, null=True)
    category = models.ForeignKey(Category, on_delete=CASCADE, default=1)
    image = models.ImageField(upload_to='uploads/images/products/')

    def __str__(self):
        return self.name

    def get_all_products():
        return Product.objects.all()

    def get_all_products_by_category_id(category_id):
        return Product.objects.filter(category_id=category_id)

    def get_product_by_id(product_id):
        return Product.objects.get(pk=product_id)

    def get_product_by_ids_list(product_ids):
        return Product.objects.filter(id__in=product_ids)
