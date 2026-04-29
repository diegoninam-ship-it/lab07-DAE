from rest_framework.routers import DefaultRouter
from .views import ReviewViewSet  # NUEVO

router = DefaultRouter()
router.register(r'reviews', ReviewViewSet, basename='reviews')  # NUEVO

urlpatterns = router.urls