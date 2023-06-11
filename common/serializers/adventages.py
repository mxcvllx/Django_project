from rest_framework import serializers

from common.models.advantages import Advantages


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = ['title']