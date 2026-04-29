from rest_framework import viewsets
from .models import Review  # NUEVO
from .serializers import ReviewSerializer  # NUEVO


# NUEVO
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('id')
    serializer_class = ReviewSerializer