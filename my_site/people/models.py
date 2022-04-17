from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=128, db_index=True, verbose_name="Страна")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Person(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Имя")
    second_name = models.CharField(max_length=30, verbose_name="Фамилия")
    biography = models.TextField(verbose_name="Биография", blank=True)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)], verbose_name="Возраст")
    country = models.ForeignKey(Country, on_delete=models.PROTECT, verbose_name="Страна")

    def __str__(self):
        return f"{self.first_name} {self.second_name}, {self.age}, country - {self.country}"

    class Meta:
        verbose_name = 'Человек'
        verbose_name_plural = 'Люди'
