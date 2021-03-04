from django.conf.urls import url
from aperetteAPI import views

urlpatterns = [
    url('aperettes$', views.aperettes_list),
    url('aperettes/(?P<pk>[0-9]+)$', views.aperette_detail),

    url('categories$', views.categories_list),
    url('categories/(?P<pk>[0-9]+)$', views.categorie_detail),

    url('ingredients$', views.ingredients_list),
    url('ingredients/(?P<pk>[0-9]+)$', views.ingredient_detail),
]