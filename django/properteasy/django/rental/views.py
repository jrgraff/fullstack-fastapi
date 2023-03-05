from django.shortcuts import render, redirect
from .models import Rental
from .forms import RentalForm
from property.models import Apartment
from datetime import datetime


def make_rental(request, pk):
    form = RentalForm
    apartment = Apartment.objects.get(pk=pk)

    if request.method == 'POST':
        filled_form = RentalForm(request.POST)
        if filled_form.is_valid():
            rental = Rental()
            rental.apartment = apartment
            rental.tenant = filled_form.cleaned_data['tenant']
            rental.rented_months = filled_form.cleaned_data['rented_months']
            rental.save()
            apartment.rent()
            return redirect('property:detail', pk)

    return render(request, 'rental/make_rental.html', {'form': form, 'apartment': apartment})


def terminate_rental(request, pk):
    rental = Rental.objects.get(pk=pk)
    rental.apartment.turn_available()
    rental.delivered_date = datetime.now()
    property = rental.apartment.property
    rental.save()

    return redirect('property:detail', property.id)
