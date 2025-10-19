from django.db import models

class Caddy(models.Model):
    LEVELS = [
        ("Senior", "Senior"),
        ("Junior", "Junior"),
        ("Student", "Student"),
        ("Single", "Single"),
    ]

    name = models.CharField(max_length=100)
    level = models.CharField(max_length=20, choices=LEVELS)
    phone = models.CharField(max_length=20, blank=True)
    availability = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name_plural = "Caddies"   # ensure the admin shows the correct plural

    def __str__(self):
        return f"{self.name} ({self.level})"
