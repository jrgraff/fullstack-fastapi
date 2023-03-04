from django.db import models
from property.models import Apartment

class Rental(models.Model):
    tenant = models.CharField(max_length=255)
    terminated = models.BooleanField(default=False)
    apartment = models.ForeignKey(Apartment, on_delete=models.CASCADE)
