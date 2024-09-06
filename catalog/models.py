from django.db import models


# Create your models here.
class SortOrder(models.TextChoices):
    ASC = 'ASC'
    DESC = 'DESC'


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    sort_order = models.CharField(choices=SortOrder.choices, default=SortOrder.ASC, max_length=30)


class Image(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    file = models.FileField(upload_to='images/')
    caption = models.CharField(max_length=255)
    sort_order = models.CharField(choices=SortOrder.choices, default=SortOrder.ASC, max_length=30)


class Parameter(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    value = models.CharField(max_length=255, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    sort_order = models.CharField(choices=SortOrder.choices, default=SortOrder.ASC, max_length=30)
