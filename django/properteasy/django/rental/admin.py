from django.contrib import admin
from .models import Rental


class ListRentals(admin.ModelAdmin):
    list_display = ('tenant', 'apartment', 'rent_date', 'delivered_date')
    search_fields = ('tenant', 'apartment')
    list_filter = ('apartment',)
    list_per_page = 10


admin.site.register(Rental, ListRentals)
