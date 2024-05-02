from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
