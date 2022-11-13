from . import views
from django.urls import path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'statuses', views.StatusViewSet, basename="statuses")

urlpatterns = [
    path('view/statuses', views.StatusList.as_view(), name="statuses-view")
]

urlpatterns += router.urls
