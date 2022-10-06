from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Gallery


def home(request):
    return render(request, 'gallery/home.html')


def dashboard(request):
    return render(request, 'dashboard/home.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        view = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get(
            'username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return view


class CreateGallery(generic.CreateView):
    model = Gallery
    fields = ['title']
    template_name = 'gallery/create_gallery.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateGallery, self).form_valid(form)
        return redirect('home')


class DetailGallery(generic.DetailView):
    model = Gallery
    template_name = 'gallery/detail_gallery.html'
