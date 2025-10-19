from django.shortcuts import render, redirect
from .models import Caddy

def caddy_list(request):
    caddies = Caddy.objects.order_by("-id")
    return render(request, "caddy_list.html", {"caddies": caddies})

def caddy_add(request):
    if request.method == "POST":
        Caddy.objects.create(
            name=request.POST.get("name"),
            level=request.POST.get("level") or "Student",
            phone=request.POST.get("phone", ""),
            availability=request.POST.get("availability", "Available"),
        )
    return redirect("home")
