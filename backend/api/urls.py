from django.urls import include, path
from rest_framework import routers

from .views import (
    DogViewSet,
    BreedViewSet,
)


router = routers.DefaultRouter()

router.register(r'dogs', DogViewSet)
router.register(r'breeds', BreedViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
