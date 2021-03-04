# Aperette

L'api aperette est une api consacrée au stockage d'un aperette, qui sera utilisée de manière à ce que, en fonction de l'acool sélectionné, on affiche les données de
de l'aperette en fonction de ce dernier.
Un aperette est une sorte d'accompagnement pour cocktail. Cela peut être, par exemple, des petits fours, des crudités etc.

# Les possibilités d'actions: 
  - Lire les données de tous les aperettes
  - Lire les données d'un seul aperette
  - Ajouter un aperette
  - Modifier un aperette
  - Lire les données d'un ingrédient
  - Lire les données d'un seul ingrédient
  - Ajouter un ingrédient
  - Modifier un ingrédient
  - Lire les données d'une catégorie
  - Lire les données d'une seule catégorie
  - Ajouter une catégorie
  - Modifier une catégorie
  
# Création de la base de données 
se placer dans un terminal mysql puis :
  - create database aperette;
  - create user 'aperette'@'localhost' identified by 'Epsi2021!';
  - grant all privileges on aperette.* to 'aperette'@'localhost';

# Lancement de l'api en localhost branche master:
  - cd Aperette/
  - source venvs/aperette/bin/activate
  - pip install -r requirements.txt (le document texte requirements permet d'installer d'un seul coup toutes les dépendances python dont on aura besoin)
  - python (ou py selon ce qui fonctionne chez vous) manage.py migrate aperetteApi
  - si il vous dis de faire un python manage.py migrate tout simple, faites le)
  - python manange.py runserver
  
 Adresses des différentes actions :
  - GET
      - http://127.0.0.1:8000/ingredients
      - http://127.0.0.1:8000/categories
      - http://127.0.0.1:8000/aperettes
   
  - GET avec ID
      - http://127.0.0.1:8000/ingredients/1
      - http://127.0.0.1:8000/categories/1
      - http://127.0.0.1:8000/aperettes/1
      
  - POST
      - http://127.0.0.1:8000/ingredients
      - http://127.0.0.1:8000/categories
      - http://127.0.0.1:8000/aperettes
  - PUT 
      - http://127.0.0.1:8000/ingredients
      - http://127.0.0.1:8000/categories
      - http://127.0.0.1:8000/aperettes
