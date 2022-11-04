from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'statuses', views.StatusViewSet, basename="statuses")

urlpatterns = router.urls
