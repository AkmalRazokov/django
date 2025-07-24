from django.shortcuts import render, redirect, HttpResponse
from .models import *
from accounts.models import CustomUser

def movie_list_view(request):
    genres = Genre.objects.all()
    user = CustomUser.objects.all()
    if request.method == "GET":
        return render(request, "movie_list.html", {'genres':genres, 'user':user})


def movie_create_view(request):
    genres = Genre.objects.all()
    user
    if request.method == "GET":
        return render(request, 'movie_create.html', {'genres':genres})
    elif request.method == "POST":
        title = request.POST.get('title', False)
        description = request.POST.get('description', False)
        rating = request.POST.get('rating', False)
        genre_id = request.POST.get('genre', False)
        image = request.POST.get('image', False)
        if not title or not description or not rating or not genre_id:
            return HttpResponse('Please fill inputs')
        user = CustomUser.objects.filter()
        

