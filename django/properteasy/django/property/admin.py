from django.contrib import admin
from .models import Property, Apartment

class ListApartments(admin.ModelAdmin):
    list_display = ("number", "owner", "property")
    list_display_links = ("number","owner")
    search_fields = ("owner","number")
    list_filter = ("property",)
    list_per_page = 10

class ListProperty(admin.ModelAdmin):
    list_display = ("name", "address")


admin.site.register(Property, ListProperty)
admin.site.register(Apartment, ListApartments)
