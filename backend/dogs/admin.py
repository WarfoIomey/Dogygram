from django.contrib import admin

from .models import Breed, Dog


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Породы."""

    list_display = (
        'id',
        'name',
        'size',
        'friendliness',
        'trainability',
        'shedding_amount',
        'exercise_needs',
    )
    list_filter = ('size',)
    empty_value_display = '-пусто-'
    search_fields = ('name',)


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    """Административный интерфейс для модели Собаки."""

    list_display = (
        'id',
        'name',
        'age',
        'gender',
        'color',
        'favorite_food',
        'favorite_toy',
        'breed'
    )
    list_filter = ('gender', 'breed')
    search_fields = ('name', 'color', 'age')
    empty_value_display = '-пусто-'
