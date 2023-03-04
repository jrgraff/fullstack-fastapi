from django.db import models


class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Apartment(models.Model):
    number = models.IntegerField()
    owner = models.CharField(max_length=255)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'Apartment: {self.number}, Property: {self.property}'
