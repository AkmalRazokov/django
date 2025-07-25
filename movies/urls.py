from .views import *
from django.urls import path

urlpatterns = [
    path('movies/', movie_list, name='movie_list'),
    path('movies/<int:pk>/', movie_detail, name='movie_detail'),
    path('movies/create/', movie_create, name='movie_create'),
    path('movies/<int:movie_id>/seances/', movie_seances, name='movie_seances'),
    path('seance/<int:seance_id>/book/', seance_book, name='seance_book')
]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)