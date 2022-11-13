from . import views
from django.urls import path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'countries', views.CountryViewSet, basename="countries")

urlpatterns = [
    path('view/countries', views.CountryList.as_view(), name="countries-view")
]

urlpatterns += router.urls
