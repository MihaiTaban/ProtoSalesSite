from django.urls import path

from . import views

app_name = "Products"
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/',views.registerPage,name = 'register'),
    path('logout/',views.logoutPage,name='logout'),
    path('login/',views.loginPage,name='login'),
    path('welcome/',views.SiteRegisterLoginLogout,name='welcome')

]