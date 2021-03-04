from django.db import models

# Create your models here.


class Categorie(models.Model):
    nom = models.CharField(max_length=70, blank=False, default='')

class Ingredient(models.Model):
    nom = models.CharField(max_length=100, blank=False, default='')
    photo = models.ImageField(
        blank=True,
        null=True,
        max_length=255
    )


class Aperette(models.Model):
    nom = models.CharField(max_length=100, blank=False, default='')
    photo = models.ImageField(
        blank=True,
        null=True,
        max_length=255
    )
    recette = models.BooleanField(default=False)
    proportions = models.IntegerField()
    alcoolAssocie = models.CharField(max_length=100, blank=False, default='')
    categories = models.ManyToManyField(Categorie)
    ingredients = models.ManyToManyField(Ingredient, blank=True, null=True)

