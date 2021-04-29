from django.urls import path, include
from rest_framework import routers
from api.views import MovieViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)

urlpatterns = [
    path('', include(router.urls))
]
