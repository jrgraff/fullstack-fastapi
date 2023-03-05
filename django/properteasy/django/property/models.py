from django.db import models


class Property(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'

    def __str__(self) -> str:
        return self.name


class Apartment(models.Model):
    STATUS_CHOICES = [
        ('av', 'Available'),
        ('um', 'Under Maintanance'),
        ('oc', 'Occupied'),
        ('dc', 'Decomisioned'),
    ]

    number = models.IntegerField()
    owner = models.CharField(max_length=255)
    month_value = models.DecimalField(max_digits=8, decimal_places=2)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=5, choices=STATUS_CHOICES, default='av')

    def __str__(self) -> str:
        return f'Property: {self.property}, Apartment: {self.number}'

    def rent(self):
        self.status = 'oc'
        self.save()

    def turn_available(self):
        self.status = 'av'
        self.save()
