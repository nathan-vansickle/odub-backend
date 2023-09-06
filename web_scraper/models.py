from django.db import models

class SaleItem(models.Model):
    name = models.CharField(max_length=100) 
    price = models.CharField(max_length=10)
    vendor = models.CharField(max_length=50)
    link = models.CharField(max_length=250)
    image = models.CharField(max_length=250)

    def __str__(self):
        return self.name