from django.db import models

class SaleItem(models.Model):
    name = models.CharField(max_length=100) 
    price = models.DecimalField(max_digits=5, decimal_places=2)
    vendor = models.CharField(max_length=50)
    link = models.URLField()
    image = models.ImageField()

    def __str__(self):
        return self.name