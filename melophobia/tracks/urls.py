from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'tracks', views.TrackViewSet, basename="tracks")
router.register(r'track-isrc', views.TrackIsrcViewSet, basename="track-isrc")
router.register(r'track-iswc', views.TrackIswcViewSet, basename="track-iswc")
router.register(r'track-types', views.TrackTypeViewSet, basename="track-types")

urlpatterns = router.urls
