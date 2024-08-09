from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    categ = models.ForeignKey(Category, on_delete=models.PROTECT)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True
    )
    image = models.ImageField(upload_to='static/products/images')
    info = models.TextField(null=True, blank=True)

    weight = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False
    )
    energy_value = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False,
        blank=False
    )
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()
    is_new = models.BooleanField()
