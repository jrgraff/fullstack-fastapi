from django.urls import path

from rental import views


app_name = 'rental'

urlpatterns = [
    path('<int:pk>/create', views.make_rental, name='create'),
    path('<int:pk>/terminate', views.terminate_rental, name='terminate'),
]
