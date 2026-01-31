from django.db import models

# Create your models here.

class Bike(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mileage = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.model}"
