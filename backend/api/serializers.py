from rest_framework import serializers

from dogs.models import Breed, Dog


class BreedSerializer(serializers.ModelSerializer):
    """Сериализатор модели Breed с подсчётом количества собак."""

    count_dogs = serializers.IntegerField(read_only=True)

    class Meta:
        model = Breed
        fields = (
            'id',
            'name',
            'size',
            'friendliness',
            'trainability',
            'shedding_amount',
            'exercise_needs',
            'count_dogs'
        )


class DogSerializer(serializers.ModelSerializer):
    """Сериализатор модели Dog с средним возрастом породы."""

    avg_breed_age = serializers.FloatField(read_only=True)

    class Meta:
        model = Dog
        fields = (
            'id',
            'name',
            'age',
            'gender',
            'color',
            'favorite_food',
            'favorite_toy',
            'breed',
            'avg_breed_age'
        )


class DogDetailSerializer(serializers.ModelSerializer):
    """Детальный сериализатор модели Dog с количеством собак этой породы."""

    count_dogs_breeds = serializers.SerializerMethodField()

    class Meta:
        model = Dog
        fields = (
            'id',
            'name',
            'age',
            'gender',
            'color',
            'favorite_food',
            'favorite_toy',
            'breed',
            'count_dogs_breeds'
        )

    def get_count_dogs_breeds(self, obj):
        """
        Возвращает количество собак данной породы.

        Args:
            obj: Экземпляр модели Dog

        Returns:
            int: Количество собак этой же породы
        """
        return obj.breed.dogs.count()
