from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Customer (models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=15)
    special_requirements = models.TextField(blank=True)
    updated = models.BooleanField(default=True)

class Restaurant(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    opening_time = models.IntegerField()
    closing_time = models.IntegerField()


class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    size = models.IntegerField()


class Reservations(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    people = models.IntegerField()
    reservation_date_time_start = models.DateTimeField()
    reservation_date_time_end = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

class Meta:
        ordering = ["created_on"]