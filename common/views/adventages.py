from rest_framework import generics

from common.models.advantages import Advantages
from common.serializers import Advantages


class AdvantagesListAPIView(generics.ListAPIView):
    queryset = Advantages.objects.all()
    serializer_class = Advantages
