from rest_framework import viewsets

from core.mixins import DetailedViewSetMixin
from pet.filter import PetFilter, PetOwnerFilter
from pet.models import Pet, PetOwner
from pet.serializers import (
    PetOwnerSerializer,
    PetSerializer,
)


class PetViewSet(DetailedViewSetMixin, viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filterset_class = PetFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(customer=user)

class PetOwnerViewSet(viewsets.ModelViewSet):
    queryset = PetOwner.objects.all()
    serializer_class = PetOwnerSerializer
    filterset_class = PetOwnerFilter
