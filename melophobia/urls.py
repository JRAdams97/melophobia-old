"""melophobia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers

router = routers.SimpleRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('artists-app/', include(('melophobia.artists.urls', 'artists'), namespace='artists')),
    path('countries-app/', include(('melophobia.countries.urls', 'countries'), namespace='countries')),
    path('genres-app/', include(('melophobia.genres.urls', 'genres'), namespace='genres')),
    path('labels-app/', include(('melophobia.labels.urls', 'labels'), namespace='labels')),
    path('languages-app/', include(('melophobia.languages.urls', 'languages'), namespace='languages')),
    path('media-app/', include(('melophobia.media.urls', 'media'), namespace='media')),
    path('producers-app/', include(('melophobia.producers.urls', 'producers'), namespace='producers')),
    path('releases-app/', include(('melophobia.releases.urls', 'releases'), namespace='releases')),
    path('statuses-app/', include(('melophobia.statuses.urls', 'statuses'), namespace='statuses')),
    path('tracks-app/', include(('melophobia.tracks.urls', 'tracks'), namespace='tracks')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
