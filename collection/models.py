from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

BRAND_CHOICES = [
    ("fendi", "fendi"),
    ("balenciaga", "balenciaga"),
]


class Collection(models.Model):
    collection = models.ImageField(blank=False, null=False, upload_to="./media/collection")
    brand = models.CharField(max_length=40, choices=BRAND_CHOICES)