from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    icon = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, db_index=True)


class Shop(models.Model):
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100, db_index=True)
    desc = models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, db_index=True)


class Review(models.Model):
    shop = models.ForeignKey(Shop)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    photo = models.ImageField(blank=True)
    rating = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    message = models.TextField()


class Item(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    desc = models.TextField(blank=True)
    amount = models.PositiveIntegerField()
    photo = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, db_index=True)


# class Order(models.Model):
#    pass

