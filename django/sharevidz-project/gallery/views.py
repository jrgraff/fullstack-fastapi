from encodings import search_function
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, JsonResponse
from django.forms.utils import ErrorList
from .models import Gallery, Video
from .forms import VideoForm, SearchForm
import urllib
import requests

YOUTUBE_API_KEY = 'AIzaSyDQlLxz7q__97njJGToO0aky4hggZYdpnY'

def home(request):
    return render(request, 'gallery/home.html')


def dashboard(request):
    galleries = Gallery.objects.filter(user=request.user)
    return render(request, 'gallery/dashboard.html', {'galleries': galleries})


def add_video(request, pk):
    form = VideoForm()
    search_form = SearchForm()
    gallery = Gallery.objects.get(pk=pk)
    if not gallery.user == request.user:
        raise Http404

    if request.method == 'POST':  # Create
        filled_form = VideoForm(request.POST)
        if filled_form.is_valid():
            video = Video()
            video.gallery = gallery
            video.url = filled_form.cleaned_data['url']
            parsed_url = urllib.parse.urlparse(video.url)
            video_id = urllib.parse.parse_qs(parsed_url.query).get('v')
            
            if video_id:
                video.youtube_id = video_id[0]
                response = requests.get(f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={ video_id[0] }&key={ YOUTUBE_API_KEY }')
                json = response.json()
                video.title = json['items'][0]['snippet']['title']
                video.save()
                return redirect('detail_gallery', pk)
            else:
                errors = form.errors.setdefault('url', ErrorList())
                errors.append('Needs to be a Youtube URL')

    return render(request, 'gallery/add_video.html', {'form': form, 'search_form': search_form, 'gallery': gallery})


def video_search(request):
    search_form = SearchForm(request.GET)
    if search_form.is_valid():
        encoded_search_term = urllib.parse.quote(search_form.cleaned_data['search_term'])
        response = requests.get(f'https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=6&q={ encoded_search_term }&key={ YOUTUBE_API_KEY }')
        return JsonResponse(response.json())
    return JsonResponse({'error': 'Not able to validate form'})


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

class DeleteVideo(generic.DeleteView):
    model = Video
    template_name = 'gallery/delete_video.html'
    fields = ['title']
    success_url = reverse_lazy('dashboard')
