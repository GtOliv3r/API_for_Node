from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from api.views import VariaveisListCreate

urlpatterns = [
    path('variaveis/', VariaveisListCreate.as_view(), name='variaveis-list-create'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
]