from django.db import models
from shop.models import *
# Create your models here.
class CartList(models.Model):
    card_id = models.CharField(max_length=200,unique=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.card_id

class Items(models.Model):
    prodt = models.ForeignKey(Products,on_delete=models.CASCADE)
    cart = models.ForeignKey(CartList,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.prodt

    def total(self):
        return self.prodt.offerprice*self.quantity

