from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from aperetteAPI.models import Aperette, Categorie, Ingredient
from aperetteAPI.serializers import AperetteSerializer, CategorieSerializer, IngredientSerializer

from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def aperettes_list(request):
    if request.method == 'GET':
        aperettes = Aperette.objects.all()

        nom = request.GET.get('nom', None)
        if nom is not None:
            aperettes = aperettes.filter(nom__icontains=nom)

        aperettes_serializer = AperetteSerializer(aperettes, many=True)
        return JsonResponse(aperettes_serializer.data, safe=False)

    elif request.method == 'POST':
        aperette_data = JSONParser().parse(request)
        aperette_serializer = AperetteSerializer(data=aperette_data)
        if aperette_serializer.is_valid():
            aperette_serializer.save()
            return JsonResponse(aperette_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(aperette_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def aperette_detail(request, pk):
    try:
        aperette = Aperette.objects.get(pk=pk)
    except Aperette.DoesNotExist:
        return JsonResponse({'message': 'Cet aperette n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        aperette_serializer = AperetteSerializer(aperette)
        return JsonResponse(aperette_serializer.data)

    elif request.method == 'PUT':
        aperette_data = JSONParser().parse(request)
        aperette_serializer = AperetteSerializer(aperette, data=aperette_data)
        if aperette_serializer.is_valid():
            aperette_serializer.save()
            return JsonResponse(aperette_serializer.data)
        return JsonResponse(aperette_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def categories_list(request):
    if request.method == 'GET':
        categories = Categorie.objects.all()

        nom = request.GET.get('nom', None)
        if nom is not None:
            categories = categories.filter(nom__icontains=nom)

        categories_serializer = CategorieSerializer(categories, many=True)
        return JsonResponse(categories_serializer.data, safe=False)

    elif request.method == 'POST':
        categorie_data = JSONParser().parse(request)
        categorie_serializer = CategorieSerializer(data=categorie_data)
        if categorie_serializer.is_valid():
            categorie_serializer.save()
            return JsonResponse(categorie_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(categorie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT'])
def categorie_detail(request, pk):
    try:
        categorie = Categorie.objects.get(pk=pk)
    except Categorie.DoesNotExist:
        return JsonResponse({'message': 'Cette catégorie n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        categorie_serializer = CategorieSerializer(categorie)
        return JsonResponse(categorie_serializer.data)

    elif request.method == 'PUT':
        categorie_data = JSONParser().parse(request)
        categorie_serializer = CategorieSerializer(categorie, data=categorie_data)
        if categorie_serializer.is_valid():
            categorie_serializer.save()
            return JsonResponse(categorie_serializer.data)
        return JsonResponse(categorie_serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def ingredients_list(request):
    if request.method == 'GET':
        ingredients = Ingredient.objects.all()

        nom = request.GET.get('nom', None)
        if nom is not None:
            ingredients = ingredients.filter(nom__icontains=nom)

        ingredients_serializer = IngredientSerializer(ingredients, many=True)
        return JsonResponse(ingredients_serializer.data, safe=False)

    elif request.method == 'POST':
        ingredient_data = JSONParser().parse(request)
        ingredient_serializer = IngredientSerializer(data=ingredient_data)
        if ingredient_serializer.is_valid():
            ingredient_serializer.save()
            return JsonResponse(ingredient_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(ingredient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def ingredient_detail(request, pk):
    try:
        ingredient = Ingredient.objects.get(pk=pk)
    except Ingredient.DoesNotExist:
        return JsonResponse({'message': 'Cet ingrédient n\'existe pas'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        ingredient_serializer = IngredientSerializer(ingredient)
        return JsonResponse(ingredient_serializer.data)

    elif request.method == 'PUT':
        ingredient_data = JSONParser().parse(request)
        ingredient_serializer = IngredientSerializer(ingredient, data=ingredient_data)
        if ingredient_serializer.is_valid():
            ingredient_serializer.save()
            return JsonResponse(ingredient_serializer.data)
        return JsonResponse(ingredient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
