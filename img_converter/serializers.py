from rest_framework import serializers
from . import models


class ImagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Images
        fields = '__all__'
