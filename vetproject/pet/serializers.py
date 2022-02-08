from rest_framework import serializers

from pet.models import Pet, PetOwner


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ("id", "name", "type", "variety", "explain")


class PetOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ("id", "name")


