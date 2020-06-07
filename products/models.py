from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):

    objects = models.Manager()

    PLANTS = 'plants'
    SEEDS = 'seeds'
    EQUIPTMENT = 'equiptment'
    OTHER = 'other'

    CATEGORY = [
        (PLANTS, 'plants'),
        (SEEDS, 'seeds'),
        (EQUIPTMENT, 'equiptment'),
        (OTHER, 'other'),
    ]

    category = models.CharField(
        max_length=20,
        choices=CATEGORY,
        default=OTHER,
    )

    name = models.CharField(
        max_length=254, default=''
    )

    description = models.TextField()

    price = models.DecimalField(
        max_digits=6, decimal_places=2
    )

    image = models.ImageField(
        upload_to='images'
    )

    def __str__(self):
        return self.name
