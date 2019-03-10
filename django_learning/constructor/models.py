from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=255)


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    group = models.ForeignKey(Group, on_delete=None)
