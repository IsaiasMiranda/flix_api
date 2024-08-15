from django.db import models


class Genre(models.Model):
    genre = models.CharField(max_length=160)

    class Meta:
        db_table = 'api_genre'
        
    def __str__(self):
        return self.genre
