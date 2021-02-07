from django.db import models

# Create your models here.

class ProductSectionsDB(models.Model):
    Sections = models.CharField(max_length=200)

class SkiDB(models.Model):
    Brand = models.CharField(max_length=200)
    Size = models.IntegerField(200)
    Availability = models.IntegerField(200)

class SnowboardDB(models.Model):
    Brand = models.CharField(max_length=200)
    Size = models.IntegerField(200)
    Availability = models.IntegerField(200)

class SkiBootsDB(models.Model):
    Brand = models.CharField(max_length=200)
    Size = models.IntegerField(200)
    Availability = models.IntegerField(200)

class SnowboardBootsDB(models.Model):
    Brand = models.CharField(max_length=200)
    Size = models.IntegerField(200)
    Availability = models.IntegerField(200)

