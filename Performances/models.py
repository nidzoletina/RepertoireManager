from django.db import models
# from 
# Create your models here.

from Repertoire.models import song

class Performance(models.Model):
	def __str__(self):
		return self.name

	name = models.CharField(max_length=200)
	songs = models.ManyToManyField(song, through='SongOrder')
	date = models.DateField(null=True, blank=True)

class SongOrder(models.Model):
	def __str__(self):
		return self.songs.name

	songs = models.ForeignKey(song, on_delete=models.CASCADE)
	performance = models.ForeignKey(Performance, on_delete=models.CASCADE)
	orderInPerformance = models.IntegerField(null=True, blank=True)