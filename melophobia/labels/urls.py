from . import views
from django.urls import path, include
from rest_framework_nested.routers import NestedSimpleRouter, SimpleRouter

router = SimpleRouter()
router.register(r'labels', views.LabelViewSet, basename="labels")

catalogue_router = NestedSimpleRouter(router, r'labels', lookup='label')
catalogue_router.register(r'catalogue', views.CatalogueItemsViewSet, basename='catalogue')

urlpatterns = [
    path('view/labels', views.LabelList.as_view(), name="labels-view")
]

urlpatterns += [
    path('', include(router.urls)),
    path('', include(catalogue_router.urls)),
]
