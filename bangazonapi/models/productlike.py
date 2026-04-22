from django.db import models
from .customer import Customer
from .product import Product

class ProductLike(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="liked_products"
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="likes"
    )

    class Meta:
        unique_together = ("customer", "product")
        verbose_name = "productlike"
        verbose_name_plural = "productlikes"