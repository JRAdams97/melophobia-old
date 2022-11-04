from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'genres', views.GenreViewSet, basename="genres")

urlpatterns = router.urls