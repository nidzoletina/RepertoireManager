from django.contrib import admin

# Register your models here.
# from Repertoire.models import song
from .models import SongOrder, Performance, song

class SongOrderInLine(admin.TabularInline):
	model = SongOrder
	extra = 1

class PerformanceAdmin(admin.ModelAdmin):
	# list_display = ('name', SongOrderInLine)
	inlines = (SongOrderInLine,)

# class SongAdmin(admin.ModelAdmin):
# 	inlines = (song, )


admin.site.register(Performance, PerformanceAdmin)
admin.site.register(song)