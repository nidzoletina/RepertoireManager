from django.db import models

# Create your models here.

class song(models.Model):
	name = models.CharField(max_length=200)
	lyrics = models.TextField(null=True, blank=True)
	audioFile = models.FileField(upload_to='audioRepository', null=True, blank=True)

	def __str__(self):
		return self.name
