from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=225,unique=True)
    language=models.CharField(max_length=225)
    run_time=models.PositiveIntegerField()
    genre=models.CharField(max_length=225)
    director=models.CharField(max_length=225)
    actors=models.CharField(max_length=225)
    year=models.PositiveIntegerField()
    
    def __str__(self):
        return self.name