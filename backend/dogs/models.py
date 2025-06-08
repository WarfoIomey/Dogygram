from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

import dogs.constants as constants


User = get_user_model()


class Breed(models.Model):

    name = models.CharField(
        help_text='Укажите назваине породы',
        verbose_name='Порода',
        max_length=constants.MAX_LENGTH_NAME,
    )
    size = models.CharField(
        help_text='Выбирете размер собаки',
        choices=constants.SIZE_BREED,
        verbose_name='Размер собаки'
    )
    friendliness = models.PositiveSmallIntegerField(
        help_text='Укажите уровень дружелюбия от 1 до 5',
        verbose_name='Дружелюбие',
        validators=[
            MinValueValidator(constants.MIN_LEVEL),
            MaxValueValidator(constants.MAX_LEVEL)
        ],
    )
    trainability = models.PositiveSmallIntegerField(
        help_text='Укажите уровень обучаемости от 1 до 5',
        verbose_name='Обучаемость',
        validators=[
            MinValueValidator(constants.MIN_LEVEL),
            MaxValueValidator(constants.MAX_LEVEL)
        ],
    )
    shedding_amount = models.PositiveSmallIntegerField(
        help_text='Укажите количество линьки от 1 до 5',
        verbose_name='Количество линьки',
        validators=[
            MinValueValidator(constants.MIN_LEVEL),
            MaxValueValidator(constants.MAX_LEVEL)
        ],
    )
    exercise_needs = models.PositiveSmallIntegerField(
        help_text='Укажите длительность физической активности 1 до 5',
        verbose_name='Физическая активность',
        validators=[
            MinValueValidator(constants.MIN_LEVEL),
            MaxValueValidator(constants.MAX_LEVEL)
        ],
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Порода'
        verbose_name_plural = 'Породы'


class Dog(models.Model):
    name = models.CharField(
        max_length=constants.MAX_LENGTH_NAME,
        verbose_name='Имя собаки',
        help_text='Укажите имя собаки',
    )
    age = models.PositiveSmallIntegerField(
        help_text='Укажите возраст собаки от 0 до 20 лет',
        verbose_name='Возраст собаки',
        validators=[
            MinValueValidator(constants.MIN_AGE_DOG),
            MaxValueValidator(constants.MAX_AGE_DOG)
        ],
    )
    gender = models.CharField(
        help_text='Выберите пол собаки',
        verbose_name='Пол собаки',
        choices=constants.GENDER_CHOICE,
    )
    color = models.CharField(
        help_text='Укажите цвет собаки',
        verbose_name='Цвет собаки',
        max_length=constants.MAX_LENGTH_COLOR,
    )
    favorite_food = models.CharField(
        help_text='Укажите любимую еду',
        verbose_name='Любимая еда',
        max_length=constants.MAX_LENGTH_FOOD,
    )
    favorite_toy = models.CharField(
        help_text='Укажите любимую игрушку',
        verbose_name='Любимая игрушка',
        max_length=constants.MAX_LENGTH_TOY,
    )
    breed = models.ForeignKey(
        Breed,
        help_text='Укажите породу собаки',
        on_delete=models.CASCADE,
        related_name='dogs',
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Собака'
        verbose_name_plural = 'Собаки'
