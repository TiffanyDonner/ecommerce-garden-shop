from django.db import models


# Create your models here.
class Product(models.Model):

    objects = models.Manager()

    PLANTS = 'Plants'
    SEEDS = 'Seeds'
    EQUIPTMENT = 'Equiptment'
    OTHER = 'Other'

    CATEGORY_CHOICES = [
        (PLANTS, 'Plants'),
        (SEEDS, 'Seeds'),
        (EQUIPTMENT, 'Equiptment'),
        (OTHER, 'Other'),
    ]

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
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
