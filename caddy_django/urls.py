from django.contrib import admin
from django.urls import path
from core.views import caddy_list, caddy_add

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", caddy_list, name="home"),
    path("caddies/add/", caddy_add, name="caddy_add"),
]


