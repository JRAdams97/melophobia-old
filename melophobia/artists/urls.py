from . import views
from django.urls import path
from rest_framework.routers import SimpleRouter


router = SimpleRouter()
router.register(r'artists', views.ArtistViewSet, basename="artists")
router.register(r'artist-types', views.ArtistTypeViewSet, basename="artistTypes")
router.register(r'ipis', views.IpiViewSet, basename="ipi")

urlpatterns = [
    path('view/artist/<int:pk>', views.ArtistDetail.as_view(), name="artist-detail-view"),
    path('view/artist/<int:pk>/update', views.ArtistUpdate.as_view(), name="artist-update-view"),
    path('view/artist/<int:pk>/delete', views.ArtistDelete.as_view(), name="artist-delete-view"),
    path('view/artists', views.ArtistList.as_view(), name="artists-view"),
    path('view/artist', views.ArtistCreate.as_view(), name="artist-create-view"),
    path('view/artist_types', views.ArtistTypeList.as_view(), name="artist-types-view")
]

urlpatterns += router.urls
