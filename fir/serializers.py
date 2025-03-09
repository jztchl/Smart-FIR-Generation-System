from rest_framework import serializers
from .models import FIR

class FIRSerializer(serializers.ModelSerializer):
    class Meta:
        model = FIR
        fields = '__all__'
