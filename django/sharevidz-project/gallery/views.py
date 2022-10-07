from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .models import Gallery, Video
from .forms import VideoForm, SearchForm


def home(request):
    return render(request, 'gallery/home.html')


def dashboard(request):
    return render(request, 'gallery/dashboard.html')


def add_video(request, pk):
    form = VideoForm()
    search_form = SearchForm()

    if request.method == 'POST':  # Create
        filled_form = VideoForm(request.POST)
        if filled_form.is_valid():
            video = Video()
            video.url = filled_form.cleaned_data['url']
            video.youtube_id = filled_form.cleaned_data['youtube_id']
            video.title = filled_form.cleaned_data['title']
            video.gallery = Gallery.objects.get(pk=pk)
            video.save()

    return render(request, 'gallery/add_video.html', {'form': form, 'search_form': search_form})


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
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        super(CreateGallery, self).form_valid(form)
        return redirect('home')


class DetailGallery(generic.DetailView):
    model = Gallery
    template_name = 'gallery/detail_gallery.html'


class UpdateGallery(generic.UpdateView):
    model = Gallery
    template_name = 'gallery/update_gallery.html'
    fields = ['title']
    success_url = reverse_lazy('dashboard')


class DeleteGallery(generic.DeleteView):
    model = Gallery
    template_name = 'gallery/delete_gallery.html'
    fields = ['title']
    success_url = reverse_lazy('dashboard')
