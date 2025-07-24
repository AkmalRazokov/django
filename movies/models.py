from django.db import models

class Genre(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table= 'genre'
        verbos_name = 'Genre'
        verbos_name_plural = 'Genres'

    

class Movie(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    genre = models.ForeignKey(Genre, related_name='genre_id', on_delete=models.CASCADE)
    description = models.TextField()
    rating = models.IntegerField()
    image = models.ImageField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table= 'movie'
        verbos_name = 'Movie'
        verbos_name_plural = 'Movies'


class Session(models.Model):
    movie = models.ForeignKey(Movie, related_name='sess', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank=True)
    quantity = models.IntegerField()
    occupied_places = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table= 'session'
        verbos_name = 'Session'
        verbos_name_plural = 'Sessions'



