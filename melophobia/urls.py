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
from django.urls import include, path
from rest_framework import routers

router = routers.SimpleRouter()

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('artists-app/', include('melophobia.artists.urls')),
    path('countries-app/', include('melophobia.countries.urls')),
    path('genres-app/', include('melophobia.genres.urls')),
    path('labels-app/', include('melophobia.labels.urls')),
    path('languages-app/', include('melophobia.languages.urls')),
    path('media-app/', include('melophobia.media.urls')),
    path('producers-app/', include('melophobia.producers.urls')),
    path('releases-app/', include('melophobia.releases.urls')),
    path('statuses-app/', include('melophobia.statuses.urls')),
    path('tracks-app/', include('melophobia.tracks.urls')),
]
