from rest_framework.permissions import BasePermission
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class PhoneNumberValidator(RegexValidator):
    """
    Validator for phone numbers.
    """

    regex = r"^\+[0-9]{1,3}\d{10}$"
    message = _(
        "Phone number must be entered in the format: +901234567890. "
        "Up to 13 digits allowed."
    )
    flags = 0

class IsStaffUserAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.is_authenticated and request.user.is_staff
        )


class IsNotAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return not bool(request.user and request.user.is_authenticated)
