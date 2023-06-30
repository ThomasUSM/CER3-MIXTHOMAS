from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClaseSerializers
from .models import Clase


class ClaseViewSet(viewsets.ModelViewSet):
    queryset = Clase.objects.all()
    serializer_class = ClaseSerializers

def home(request):
    return render(request, 'astro_gym/base.html')