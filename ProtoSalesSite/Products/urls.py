from django.urls import path

from . import views

app_name = "Products"
urlpatterns = [
    path('', views.homepage, name='homepage'),

]