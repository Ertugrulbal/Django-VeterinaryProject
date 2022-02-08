"""vetproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from vetproject.router import router
from django.urls import include, path
from pet.views import PetViewSet, PetOwnerViewSet
from core.views import APITokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

router.register("pets", PetViewSet)
router.register("petowners", PetOwnerViewSet)
urlpatterns = [
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api/token/", APITokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + [
        path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    ]