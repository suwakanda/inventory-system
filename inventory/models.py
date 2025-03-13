
from django.db import models
from django.core.validators import MinValueValidator

class Supplier(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    note = models.TextField()
    stock = models.IntegerField(validators=[MinValueValidator(0)])
    availability = models.BooleanField(default=False)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)

    def __str__(self):
        return self.name