from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def homepage(request):
    return HttpResponse("Hello, world. You're at the <strong>Products</strong> homepage.")