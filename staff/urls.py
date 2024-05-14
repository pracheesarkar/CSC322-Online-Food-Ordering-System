from django.urls import path
from .views import *



urlpatterns = [
    path('deliver/', Deliver.as_view(), name='deliver'),
    path('dashboard/', Dashboard.as_view(),name='dashboard'),
    #path('addfood/', AddFood.as_view(), name='addfood'),
    path('addfood/', addfood, name='addfood'),

    #path('error/')
]