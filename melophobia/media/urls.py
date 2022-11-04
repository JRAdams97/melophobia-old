from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'media', views.MediaViewSet, basename="media")

urlpatterns = router.urls
