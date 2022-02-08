from django.db import models
from django.utils.translation import gettext_lazy as _
from core.utils import PhoneNumberValidator
from core.models import BaseAbstractModel
from django.contrib.auth.validators import UnicodeUsernameValidator

class PetOwner(BaseAbstractModel):
    """
    PetOwner model
    """
    phonenumber_validator = PhoneNumberValidator()
    username_validator = UnicodeUsernameValidator()

    name1 = models.CharField(max_length=100, verbose_name=_("PetOwner Name"))
    surname= models.CharField(max_length=100, verbose_name=_("PetOwner SurName"))
    email = models.EmailField(
        _("email address"), unique=True, validators=[username_validator]
    )
    phone = models.CharField(
        max_length=20,
        verbose_name=_("Phone Number"),
        validators=[phonenumber_validator],
        help_text=_("Phone number must be entered in the format: +901234567890. "),
    )

    class Meta:
        verbose_name = _("Pet Owner")
        verbose_name_plural = _("Pet Owners")

    def __str__(self):
        return self.name1


class Pet(BaseAbstractModel):
    """
    Pet model
    """

    name = models.CharField(max_length=100, verbose_name=_("Name"))
    type = models.CharField(max_length=100, verbose_name=_("Type"))
    variety = models.CharField(max_length=100, verbose_name=_("Variety"))
    explain = models.CharField(max_length=100, verbose_name=_("Explain"))
    age = models.DecimalField(
        max_digits=3, decimal_places=1, verbose_name=_("Age"))
    owner = models.ForeignKey(PetOwner, verbose_name=_("Pet Owner"), on_delete=models.PROTECT)
    class Meta:
        verbose_name = _("Pet")
        verbose_name_plural = _("Pets")

    def __str__(self):
        return f"{self.name}-{self.variety}-{self.explain}"


