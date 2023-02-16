from django.shortcuts import render
from .models import Images
from .serializer import ImagesSerializer
from rest_framework import viewsets
# Create your views here.


class ImagesViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImagesSerializer
