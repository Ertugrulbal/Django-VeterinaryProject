from rest_framework import serializers

from pet.models import Pet, PetOwner


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ("id", "name", "type", "variety", "explain","age","created_at","modified_at","owner")


class PetOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ("id", "name1","surname","email","phone")


