from django.db import models

# Create your models here.

class ProductSectionsDB(models.Model):
    Sections = models.CharField(max_length=200)

class SkiDB(models.Model):
    Brand = models.CharField(max_length=200)
    Size = models.IntegerField()
    Availability = models.IntegerField()

class SnowboardDB(models.Model):
    Brand = models.CharField(max_length=200)
    Size = models.IntegerField()
    Availability = models.IntegerField()

class SkiBootsDB(models.Model):
    Brand = models.CharField(max_length=200)
    Size = models.IntegerField()
    Availability = models.IntegerField()

class SnowboardBootsDB(models.Model):
    Brand = models.CharField(max_length=200)
    Size = models.IntegerField()
    Availability = models.IntegerField()

