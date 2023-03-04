from django.urls import path

from property import views


app_name = 'property'

urlpatterns = [
    path('', views.ListProperty.as_view(), name='list'),
    path('create/', views.CreateProperty.as_view(), name='create'),
    path('<int:pk>', views.DetailProperty.as_view(),
         name='detail'),
    path('<int:pk>/update/',
         views.UpdateProperty.as_view(), name='update'),

    path('<int:pk>/create-apartment', views.create_apartment,
         name='create_apartment'),
]
