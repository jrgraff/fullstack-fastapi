from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect, render
from .models import Property, Apartment
from .forms import ApartmentForm


def create_apartment(request, pk):
    form = ApartmentForm
    property = Property.objects.get(pk=pk)

    if request.method == 'POST':  # Create
        filled_form = ApartmentForm(request.POST)
        if filled_form.is_valid():
            apartment = Apartment()
            apartment.property = property
            apartment.number = filled_form.cleaned_data['number']
            apartment.owner = filled_form.cleaned_data['owner']
            apartment.save()
            return redirect('property:detail', pk)

    return render(request, 'apartment/create_apartment.html', {'form': form, 'property': property})


class CreateProperty(LoginRequiredMixin, generic.CreateView):
    model = Property
    fields = ['name', 'address']
    template_name = 'property/create_property.html'
    success_url = reverse_lazy('property:list')


class DetailProperty(LoginRequiredMixin, generic.DetailView):
    model = Property
    template_name = 'property/detail_property.html'
# def detail_property(request, pk):
#     property = Property.objects.get(pk=pk)
#     apartments = Apartment.objects.filter(rental__terminate=false)
#     return render(request, 'gallery/dashboard.html', {'galleries': galleries})


class ListProperty(LoginRequiredMixin, generic.ListView):
    model = Property
    template_name = 'property/list_property.html'


class UpdateProperty(LoginRequiredMixin, generic.UpdateView):
    model = Property
    template_name = 'property/create_property.html'
    fields = ['name']
    success_url = reverse_lazy('dashboard')
