from django.contrib import admin

from .models import Breed, Dog


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'size',
        'friendliness',
        'trainability',
        'shedding_amount',
        'exercise_needs',
    )
    search_fields = ('name',)


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):

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
    search_fields = ('name', 'color', 'age')
