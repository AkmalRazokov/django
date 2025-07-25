from django.shortcuts import render, redirect, HttpResponse
from .models import *
from accounts.models import CustomUser


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = Movie.objects.filter(pk=pk).first()
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def movie_seances(request, movie_id):
    movie = Movie.objects.filter(pk=movie_id).first()
    if not movie:
        return HttpResponse("Фильм не найден")
    seances = Session.objects.filter(movie=movie)
    return render(request, "movies/movie_seances.html", {"movie": movie, "seances": seances})


def seance_book(request, seance_id):
    seance = Session.objects.filter(pk=seance_id).first()
    if not seance:
        return HttpResponse("Сеанс не найден")
    
    if request.method == 'POST':
        return redirect('my_tickets')

    return render(request, "seance/book.html", {"seance": seance})



def my_tickets(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, "tickets/my_tickets.html", {"tickets": tickets})


def movie_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        release_date = request.POST.get('release_date')
        duration = request.POST.get('duration_minutes')
        genre_id = request.POST.get('genre')
        image = request.FILES.get('image')

        if not title:
            return HttpResponse("Title is required")

        movie = Movie.objects.create(
            title=title,
            description=description,
            release_date=release_date,
            duration_minutes=duration,
            genre_id=genre_id,
            image=image,
        )
        return redirect('movie_detail', pk=movie.pk)

    genres = Genre.objects.all()
    return render(request, 'movies/movie_create.html', {'genres': genres})






        

