from django.urls import path
from .views import VariaveisListCreate

urlpatterns = [
    path('variaveis/', VariaveisListCreate.as_view(), name='variaveis-list-create'),
]