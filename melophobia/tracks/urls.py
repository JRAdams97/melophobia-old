from . import views
from django.urls import path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'tracks', views.TrackViewSet, basename="tracks")
router.register(r'track-isrc', views.TrackIsrcViewSet, basename="track-isrc")
router.register(r'track-iswc', views.TrackIswcViewSet, basename="track-iswc")
router.register(r'track-types', views.TrackTypeViewSet, basename="track-types")

urlpatterns = [
    path('view/tracks', views.TrackList.as_view(), name="tracks-view"),
    path('view/track-isrc', views.TrackIsrcList.as_view(), name="track-isrc-view"),
    path('view/track-iswc', views.TrackIswcList.as_view(), name="track-iswc-view"),
    path('view/track-types', views.TrackTypeList.as_view(), name="track-types-view")
]

urlpatterns += router.urls
