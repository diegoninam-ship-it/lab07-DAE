from django.contrib import admin
from .models import Review  # NUEVO


# NUEVO
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'author', 'rating')
