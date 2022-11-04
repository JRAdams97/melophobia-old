from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'producers', views.ProducerViewSet, basename="producers")

urlpatterns = router.urls