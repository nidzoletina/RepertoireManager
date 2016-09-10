from django.db import models
# from 
# Create your models here.

class Performance(models.Model):
	name = models.CharField(max_length=200)
	