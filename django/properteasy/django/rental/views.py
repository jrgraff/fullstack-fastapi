from django.shortcuts import render, redirect
from .models import Rental
from .forms import RentalForm
from property.models import Apartment

def make_rental(request, pk):
    form = RentalForm
    apartment = Apartment.objects.get(pk=pk)

    if request.method == 'POST':  # Create
        filled_form = RentalForm(request.POST)
        if filled_form.is_valid():
            rental = Rental()
            rental.apartment = apartment
            rental.tenant = filled_form.cleaned_data['tenant']
            rental.save()
            return redirect('property:detail', pk)

    return render(request, 'rental/make_rental.html', {'form': form, 'apartment': apartment})

def terminate_rental(request, pk):
    form = RentalForm
    apartment = Apartment.objects.get(pk=pk)

    if request.method == 'POST':  # Create
        filled_form = RentalForm(request.POST)
        if filled_form.is_valid():
            rental = Rental()
            rental.apartment = apartment
            rental.tenant = filled_form.cleaned_data['tenant']
            rental.save()
            return redirect('property:detail', pk)

    return render(request, 'rental/make_rental.html', {'form': form, 'apartment': apartment})