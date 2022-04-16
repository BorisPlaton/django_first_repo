from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(120)])
    country = models.CharField(max_length=120, default="USA")

    def __str__(self):
        return f"{self.name}, {self.age}, country - {self.country}"
