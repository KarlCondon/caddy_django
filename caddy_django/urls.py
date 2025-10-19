from django.contrib import admin
from django.urls import path
from core.views import caddy_list, caddy_add, caddy_update, caddy_delete

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", caddy_list, name="home"),
    path("caddies/add/", caddy_add, name="caddy_add"),
    path("caddies/<int:caddy_id>/update/", caddy_update, name="caddy_update"),
    path("caddies/<int:caddy_id>/delete/", caddy_delete, name="caddy_delete"),
]



