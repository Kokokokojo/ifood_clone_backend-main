from django.urls import path
from .views import available_categories


urlpatterns = [
    path('available-categories/', available_categories, name='available-categories'),
]
