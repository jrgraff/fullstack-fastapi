from django.db import models
from property.models import Apartment
from datetime import datetime


class Rental(models.Model):
    tenant = models.CharField(max_length=255)
    rent_date = models.DateField(default=datetime.now)
    delivered_date = models.DateField(null=True)
    rented_months = models.IntegerField(default=24)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Apartment {self.apartment} rented to {self.tenant}'
