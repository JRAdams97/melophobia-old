from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'releases', views.ReleaseViewSet, basename="releases")
router.register(r'release-types', views.ReleaseTypeViewSet, basename='release-types')
router.register(r'release-statuses', views.ReleaseStatusViewSet)
router.register(r'status', views.StatusViewSet, basename='status')

urlpatterns = router.urls
