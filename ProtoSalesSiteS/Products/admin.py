from django.contrib import admin

# Register your models here.
from .models import ProductSectionsDB,SkiDB,SkiBootsDB,SnowboardBootsDB,SnowboardDB


admin.site.register(ProductSectionsDB)
admin.site.register(SkiDB)
admin.site.register(SkiBootsDB)
admin.site.register(SnowboardDB)
admin.site.register(SnowboardBootsDB)