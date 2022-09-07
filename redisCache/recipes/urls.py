from django.urls import path
from recipes import views as api_views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
   path('recipes/',api_views.manage_items, name='recipe-list' ),
  # path('recipess/',api_views.RecipeListCreateAPIViewasd.as_view({'get': 'list'}), name='recipe-lists' ),
   path('recipes/<slug:key>', api_views.manage_item, name='recipe-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)