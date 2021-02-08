from django.contrib import admin

# Register your models here.
from .models import ProductSectionsDB,SkiDB,SkiBootsDB,SnowboardBootsDB,SnowboardDB

admin.site.register(SkiDB)