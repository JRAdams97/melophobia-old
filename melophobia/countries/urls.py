from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'countries', views.CountryViewSet, basename="countries")

urlpatterns = router.urls
