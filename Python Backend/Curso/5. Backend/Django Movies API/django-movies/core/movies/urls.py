from django.contrib import admin
from django.urls import path

from .views import index_movies, MovieView

urlpatterns = [
    path('online/', index_movies, name="index_movies"),
    path('movie/', MovieView.as_view())
]
