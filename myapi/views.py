from rest_framework import viewsets
from .serializers import HeroSerializer
from .models import Hero


class HeroViewSet(viewsets.ModelViewSet):
    quaryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer