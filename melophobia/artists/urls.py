from . import views
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'artists', views.ArtistViewSet, basename="artists")
router.register(r'artist-types', views.ArtistTypeViewSet, basename="artistTypes")
router.register(r'ipis', views.IpiViewSet, basename="ipi")

urlpatterns = router.urls
