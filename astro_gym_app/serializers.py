from rest_framework import serializers
from .models import Clase

class ClaseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Clase
        fields = '__all__'