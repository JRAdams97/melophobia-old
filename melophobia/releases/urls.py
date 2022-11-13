from . import views
from django.urls import path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'releases', views.ReleaseViewSet, basename="releases")
router.register(r'release-types', views.ReleaseTypeViewSet, basename='release-types')
router.register(r'release-statuses', views.ReleaseStatusViewSet)
router.register(r'status', views.StatusViewSet, basename='status')

urlpatterns = [
    path('view/releases', views.ReleaseList.as_view(), name="releases-view"),
    path('view/release-statuses', views.ReleaseStatusList.as_view(), name="release-statuses-view"),
    path('view/release-types', views.ReleaseTypeList.as_view(), name="release-types-view")
]

urlpatterns += router.urls
