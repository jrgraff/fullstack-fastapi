"""sharevidz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from gallery import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard', views.dashboard, name='dashboard'),

    # AUTH
    path('signup', views.SignUp.as_view(), name='signup'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    # GALLERY
    path('gallery/create', views.CreateGallery.as_view(), name='create_gallery'),
    path('gallery/<int:pk>', views.DetailGallery.as_view(), name='detail_gallery'),
    path('gallery/<int:pk>/update',
         views.UpdateGallery.as_view(), name='update_gallery'),
    path('gallery/<int:pk>/delete',
         views.DeleteGallery.as_view(), name='delete_gallery'),

    # VIDEO
    path('gallery/<int:pk>/add-video', views.add_video, name='add_video'),
    path('video/search', views.video_search, name='video_search'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
