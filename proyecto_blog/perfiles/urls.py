from django.contrib import admin
from django.urls import path, include

from perfiles.views import registro, login_view, CustomLogoutView, mi_perfil

# Son las URLS generales del proyecto

urlpatterns = [
    path('registro/', registro, name="registro"),
    path('login', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('mi-perfil/', mi_perfil, name="mi-perfil"),
]
