from django.db import models
from django.db.models import DateTimeField
from django.core.validators import RegexValidator
from django_google_maps import fields as map_fields

# Create your models here.
class FoodTruckType(models.Model):
    name = models.CharField(
        max_length=40,
        unique=True,
        verbose_name="Name"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Food Truck Type"

class FoodTruck(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True,
        verbose_name = "Name",
    )
    type = models.ForeignKey(
        FoodTruckType,
        verbose_name = "Type",
    )
    url = models.URLField(
        verbose_name = "Website",
        blank = True,
    )
    phone_regex = RegexValidator(
        regex=r'^\d{3}\-\d{3}\-\d{4}$',
        message="Phone number must be entered in the format: '999-999-9999'."
    )
    phone_number = models.CharField(
        max_length=12,
        verbose_name= "Phone Number",
        validators=[phone_regex],
        blank=True
    )
    description = models.TextField(
        verbose_name = "Description",
        blank = True,
    )
    updateNotes = models.TextField(
        verbose_name = "Update Notes",
        blank = True,
    )
    updateURL = models.URLField(
        verbose_name = "Update Website",
        blank = True
    )

    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
        verbose_name = "Food Truck"

class VenueType(models.Model):
    name = models.CharField(
        max_length=40,
        unique=True,
        verbose_name = "Name"
    )
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
        verbose_name = "Venue Type"

class Venue(models.Model):
    name = models.CharField(
        max_length=128,
        unique=True,
        verbose_name = "Name",
    )
    type = models.ForeignKey(
        VenueType,
        verbose_name = "Type",
    )
    url = models.URLField(
        verbose_name = "Website",
        blank = True,
    )
    address = map_fields.AddressField(
        max_length=200,
        verbose_name = "Address",
    )
    geolocation = map_fields.GeoLocationField(
        max_length=100,
        verbose_name = "Geo Location"
    )
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Schedule(models.Model):
    foodtruck = models.ForeignKey(
        FoodTruck,
        verbose_name = "Food Truck Name",
    )
    venue = models.ForeignKey(
        Venue,
        verbose_name = "Venue Name",
    )
    startDateTime = DateTimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name = "Start Date/Time",
    )
    endDateTime = DateTimeField(
        auto_now=False,
        auto_now_add=False,
        verbose_name = "End Date/Time",
    )
    class Meta:
        ordering = ['startDateTime']
