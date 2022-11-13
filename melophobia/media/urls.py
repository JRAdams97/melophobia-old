from . import views
from django.urls import path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'media', views.MediaViewSet, basename="media")

urlpatterns = [
    path('view/media', views.MediaList.as_view(), name="media-view")
]

urlpatterns += router.urls
