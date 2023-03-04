from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

from properteasy import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # AUTH
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('properties/', include('property.urls')),
    path('rentals/', include('rental.urls')),
]
