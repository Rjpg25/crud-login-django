from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import RedirectView


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",
        RedirectView.as_view(
            pattern_name="productos:lista",
            permanent=False,
        ),
        name="inicio",
    ),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="registration/login.html"
        ),
        name="login",
    ),
    path(
        "salir/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),
    path("productos/", include("productos.urls")),
]