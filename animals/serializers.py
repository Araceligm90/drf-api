from rest_framework import serializers
from .models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        field = ('id', 'owner', 'name', 'description', 'created_at')
        model = Animal

