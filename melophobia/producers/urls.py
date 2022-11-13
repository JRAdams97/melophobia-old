from . import views
from django.urls import path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'producers', views.ProducerViewSet, basename="producers")

urlpatterns = [
    path('view/producers', views.ProducerList.as_view(), name="producers-view")
]

urlpatterns += router.urls
