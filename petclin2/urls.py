from django.contrib import admin
from django.urls import path
from rest_framework_extensions.routers import ExtendedDefaultRouter as DefaultRouter

from agendamento.api.views import UsuarioViewSet

router = DefaultRouter()

router.register("api/usuarios", UsuarioViewSet, basename="usuarios")

urlpatterns = [
    path('admin/', admin.site.urls),
]+router.urls
