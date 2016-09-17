from django.contrib import admin

from .models import song
# Register your models here.


class SongAdmin(admin.ModelAdmin):
	pass
	# list_display = ('name', 'lyrics')

admin.site.register(song, SongAdmin)