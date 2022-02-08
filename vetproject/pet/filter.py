from django_filters import rest_framework as filters

from pet.models import Pet, PetOwner


class PetFilter(filters.FilterSet):
    class Meta:
        model = Pet
        fields = ("name", "type","variety")


class PetOwnerFilter(filters.FilterSet):
    class Meta:
        model = PetOwner
        fields = ("name1",)
