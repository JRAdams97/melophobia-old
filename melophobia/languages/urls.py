from . import views
from django.urls import path
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'languages', views.LanguageViewSet, basename="languages")

urlpatterns = [
    path('view/languages', views.LanguageList.as_view(), name="languages-view")
]

urlpatterns += router.urls
