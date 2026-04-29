from rest_framework import serializers
from .models import Review  # NUEVO


# NUEVO
class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'movie', 'author', 'comment', 'rating']