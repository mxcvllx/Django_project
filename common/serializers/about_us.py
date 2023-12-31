from rest_framework import serializers

from common.models.about_us import AboutUs


class AboutUsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False)

    class Meta:
        model = AboutUs
        fields = ['id', 'title', 'description', 'image']
