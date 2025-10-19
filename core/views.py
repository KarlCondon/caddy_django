from django.shortcuts import render, redirect, get_object_or_404
from .models import Caddy

LEVELS = ["Senior", "Junior", "Student", "Single"]

def caddy_list(request):
    caddies = Caddy.objects.order_by("-id")
    return render(request, "caddy_list.html", {"caddies": caddies, "LEVELS": LEVELS})

def caddy_add(request):
    if request.method == "POST":
        Caddy.objects.create(
            name=request.POST.get("name"),
            level=request.POST.get("level") or "Student",
            phone=request.POST.get("phone", ""),
            availability=request.POST.get("availability", "Available"),
        )
    return redirect("home")

def caddy_update(request, caddy_id):
    """Update level and/or availability (and phone if you want) for a row."""
    if request.method != "POST":
        return redirect("home")
    caddy = get_object_or_404(Caddy, id=caddy_id)

    # Only update fields present in the form
    level = request.POST.get("level")
    availability = request.POST.get("availability")
    phone = request.POST.get("phone")

    if level:
        caddy.level = level
    if availability is not None:
        caddy.availability = availability
    if phone is not None:
        caddy.phone = phone

    caddy.save()
    return redirect("home")

def caddy_delete(request, caddy_id):
    """Delete a row by id (POST only)."""
    if request.method == "POST":
        caddy = get_object_or_404(Caddy, id=caddy_id)
        caddy.delete()
    return redirect("home")
