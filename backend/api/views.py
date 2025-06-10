from django.db.models import Avg, Count
from rest_framework import viewsets

from dogs.models import Breed, Dog
from .serializers import (
    BreedSerializer,
    DogSerializer,
    DogDetailSerializer
)


class DogViewSet(viewsets.ModelViewSet):
    """Набор представлений для взаимодействия с объектами Dog."""

    queryset = Dog.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        """
        Возвращает оптимизированный набор запросов с аннотациями пород.

        Returns:
            QuerySet: Набор запросов о собаках с указанием родственных пород
                и среднего возраста породы, упорядоченный по идентификатору.
        """
        return Dog.objects.select_related('breed').annotate(
            avg_breed_age=Avg('breed__dogs__age')
        ).order_by('id')

    def get_serializer_class(self):
        """
        Возвращает соответствующий класс сериализатора, основанный на действии.

        Returns:
            Serializer: DogSerializer для действия со списком,
                DogDetailSerializer в остальных случаях.
        """
        if self.action in ('list',):
            return DogSerializer
        return DogDetailSerializer


class BreedViewSet(viewsets.ModelViewSet):
    """Набор представлений для взаимодействия с объектами Breed."""

    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def get_queryset(self):
        """
        Возвращает запросов с указанием количества собак для каждой породы.

        Returns:
            QuerySet: Набор запросов по породам, в котором указано
                количество собак, упорядоченных по идентификатору.
        """
        return Breed.objects.annotate(
            count_dogs=Count('dogs')
        ).order_by('id')
