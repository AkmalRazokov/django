from django.db import models
from django.conf import settings

class Genre(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table= 'genre'
        verbose_name = 'Genre'
        verbose_name_plural = 'Genres'

    

class Movie(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    genre = models.ForeignKey(Genre, related_name='movies', on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='movies/', null=True, blank=True)
    duration = models.PositiveIntegerField(null=True, blank=True)
    age_rating = models.CharField(max_length=10, null=True, blank=True)

    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table= 'movie'
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'


class Session(models.Model):
    movie = models.ForeignKey(Movie, related_name='sessions', on_delete=models.CASCADE)
    date = models.DateField()         
    time = models.TimeField()
    hall = models.CharField(max_length=100)
    total_seats = models.IntegerField()
    occupied_seats = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.movie.title} ({self.hall})"
    
    class Meta:
        db_table= 'session'
        verbose_name = 'Session'
        verbose_name_plural = 'Sessions'



class Ticket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tickets', on_delete=models.CASCADE)
    session = models.ForeignKey(Session, related_name='tickets', on_delete=models.CASCADE)
    seat_number = models.PositiveIntegerField()
    purchased_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('session', 'seat_number') 

    def __str__(self):
        return f"Ticket #{self.pk} for {self.session} seat {self.seat_number}"



