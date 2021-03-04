from rest_framework import serializers
from aperetteAPI.models import (Aperette, Categorie, Ingredient)

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = ('id', 'nom')

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ('id', 'nom', 'photo')

class AperetteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aperette
        fields = (
            'id',
            'nom',
            'photo',
            'recette',
            'proportions',
            'alcoolAssocie',
            'categories',
            'ingredients'
            )


