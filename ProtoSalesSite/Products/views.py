from django.shortcuts import render
from .models import ProductSectionsDB
# Create your views here.
from django.http import HttpResponse


def homepage(request):
    return render(request=request,
               template_name="Products/home.html",
                  context={"ProductSections": ProductSectionsDB.objects.all})