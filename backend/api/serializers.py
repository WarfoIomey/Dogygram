from rest_framework import serializers

from dogs.models import Breed, Dog


class BreedSerializer(serializers.ModelSerializer):

    count_dogs = serializers.SerializerMethodField()

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

    def get_count_dogs(self, obj):
        pass


class DogSerializer(serializers.ModelSerializer):
    """"""

    avg_age = serializers.SerializerMethodField()

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
            'avg_age'
        )

    def get_avg_age(self, obj):
        pass


class DogDetailSerializer(serializers.ModelSerializer):
    """"""

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
        return obj.breed.dogs.count()
