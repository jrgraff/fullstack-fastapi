from django.contrib import admin
from .models import Rental


class ListRentals(admin.ModelAdmin):
    list_display = ("tenant", "apartment", 'terminated',)
    search_fields = ("tenant", "apartment", "terminated")
    list_filter = ("tenant", "apartment",)
    list_editable = ('terminated',)
    list_per_page = 10


admin.site.register(Rental, ListRentals)
