from rest_framework import generics
from .models import Variaveis
from .serializers import VariaveisSerializer

class VariaveisListCreate(generics.ListCreateAPIView):
    queryset = Variaveis.objects.all()
    serializer_class = VariaveisSerializer