from django.contrib import admin
from django.urls import path
# from .views import ReviewView, ReviewViewByMovie
from .views import ReviewView

urlpatterns = [
    path('', ReviewView.as_view(), name='movie'),
    # path('<int:pk_movie>', ReviewViewByMovie.as_view(), name='get_review_by_movie'),
    path('<int:pk_movie>', ReviewView.as_view(), name='get_review_by_movie'),
    path('user/<str:username>/', ReviewView.as_view(), name='get_review_by_user'),
    path('review/<int:pk_review>', ReviewView.as_view(), name='update_and_delete_review')
]