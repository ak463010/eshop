from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Oder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=255, default='', blank=True)
    phone_number = models.CharField(max_length=15, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.product)

    def placeOder(self):
        self.save()

    @classmethod
    def get_products_by_customer_id(cls, id):
        return cls.objects.filter(customer_id=id).order_by('-id')
