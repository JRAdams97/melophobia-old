from . import views
from django.urls import path
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'artists', views.ArtistViewSet, basename="artists")
router.register(r'artist-types', views.ArtistTypeViewSet, basename="artistTypes")
router.register(r'ipis', views.IpiViewSet, basename="ipi")

urlpatterns = [
    path('view/artists', views.ArtistList.as_view(), name="artists-view"),
    path('view/artist_types', views.ArtistTypeList.as_view(), name="artist-types-view")
]

urlpatterns += router.urls
