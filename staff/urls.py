from django.urls import path
from .views import Dashboard, AddFood


urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('addfood/', AddFood.as_view(), name='addfood'),
]