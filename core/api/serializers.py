from rest_framework import serializers
from .models import Variaveis

class VariaveisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variaveis
        fields = '__all__'