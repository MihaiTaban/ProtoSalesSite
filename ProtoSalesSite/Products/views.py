from pyexpat.errors import messages

from django.shortcuts import render, redirect
from .models import ProductSectionsDB
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate


def homepage(request):
    return render(request=request,
               template_name="Products/home.html",
                  context={"ProductSections": ProductSectionsDB.objects.all})


def SiteRegisterLoginLogout(request):
    return render(request=request,
                  template_name="Products/SiteRegisterLoginLogout.html",
                  context={"ProductSections": ProductSectionsDB.objects.all}
                  )

def registerPage(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("Products:homepage")
        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])
    return render(request=request,
                  template_name="Products/registerPage.html",
                  context={"form":UserCreationForm})

def logoutPage(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("Products:SiteRegisterLoginLogout")

def loginPage(request):
    if request.method == "POST":
      form = AuthenticationForm(request, request.POST)
      if form.is_valid():
          username = form.cleaned_data.get('username')
          password = form.cleaned_data.get('password')
          user = authenticate(username=username,password=password)
          if user is not None:
              login(request,user)
              #messages.info(request, "You are now logged in as {username}")
              return redirect("Products:homepage")
          else:
              messages.errors(request,"invalid username or password")
      else:
          messages.errors(request, "invalid username or password")
    form = AuthenticationForm()
    return render(request, template_name="Products/loginPage.html",
                  context={"form":form})