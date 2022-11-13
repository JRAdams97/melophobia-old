from . import views
from django.urls import path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'genres', views.GenreViewSet, basename="genres")

urlpatterns = [
    path('view/genres', views.GenreList.as_view(), name="genres-view")
]

urlpatterns += router.urls
