from rest_framework import serializers
from . import models

# Serializer : custome
# ModelSerializer : Automated from model
class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Product
        fields='__all__'