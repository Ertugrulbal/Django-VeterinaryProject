from django.contrib import admin

from pet.models import Pet, PetOwner




@admin.register(PetOwner)
class PetOwnerAdmin(admin.ModelAdmin):
    """
    Admin View for PetOwners
    """

    list_display = ("name1","surname","email","phone")
    search_fields = ['name1','surname']



@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    """
    Admin View for Pet
    """

    list_display = ("name", "type","variety","explain","age","owner")
    search_fields = ['name']
