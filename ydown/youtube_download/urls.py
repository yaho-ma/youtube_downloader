from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ytb_down, name='ytb_down'),
    path('download/', views.yt_download),
    path('download_chosen_resolution/',
         views.download_chosen_resolution,
         name='download_chosen_resolution')
]
