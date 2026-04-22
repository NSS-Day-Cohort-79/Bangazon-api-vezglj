from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):
    name = models.TextField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="store")
    description = models.TextField(max_length=255)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "store"
        verbose_name_plural = "stores"

    def __str__(self):
        return self.name
