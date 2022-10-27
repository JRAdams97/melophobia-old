from rest_framework.routers import SimpleRouter
from melophobia.artists import views

router = SimpleRouter()
router.register(r'artists', views.ArtistViewSet, basename="artists")
router.register(r'artist-types', views.ArtistTypeViewSet, basename="artistTypes")

urlpatterns = router.urls
