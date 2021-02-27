from pyexpat.errors import messages

from django.shortcuts import render, redirect
from .models import ProductSectionsDB, SkiDB, SnowboardBootsDB, SnowboardDB, SkiBootsDB
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate


def homepage(request):
    if not request.user.is_authenticated:
        print("zzz")
        return redirect("Products:welcome")
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
    #messages.info(request, "Logged out successfully!")
    print("logout")
    return redirect("Products:welcome")

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
              raise Exception("Invalid password or username")
      else:
          raise Exception("Invalid password or username")
    form = AuthenticationForm()
    return render(request, template_name="Products/loginPage.html",
                  context={"form":form})

def SkiPage(request):

    if not request.user.is_authenticated:
        print("zzz")
        return redirect("Products:welcome")
    skies = SkiDB.objects.all()
    print(skies)
    data = []
    for ski in skies:
        result = {}
        result["Brand"] = ski.Brand
        result["Size"] = ski.Size
        result["Availability"] = ski.Availability
        data.append(result)
        print(data)
    return render(request=request,
                  template_name="Products/SkiPage.html",
                  context={"data": data}
                  )

def SkiBootsPage(request):

    if not request.user.is_authenticated:
        print("zzz")
        return redirect("Products:welcome")
    skiBoots = SkiBootsDB.objects.all()
    print(skiBoots)
    data = []
    for boots in skiBoots:
        result = {}
        result["Brand"] = boots.Brand
        result["Size"] = boots.Size
        result["Availability"] = boots.Availability
        data.append(result)
        print(data)
    return render(request=request,
                  template_name="Products/SkiBoots.html",
                  context={"data": data}
                  )

def SnowboardsPage(request):

    if not request.user.is_authenticated:
        print("zzz")
        return redirect("Products:welcome")
    snowboards = SnowboardDB.objects.all()
    print(snowboards)
    data = []
    for boards in snowboards:
        result = {}
        result["Brand"] = boards.Brand
        result["Size"] = boards.Size
        result["Availability"] = boards.Availability
        data.append(result)
        print(data)
    return render(request=request,
                  template_name="Products/SnowboardsPage.html",
                  context={"data": data}
                  )

def SnowboardsBootsPage(request):

    if not request.user.is_authenticated:
        print("zzz")
        return redirect("Products:welcome")
    snowBoots = SnowboardBootsDB.objects.all()
    print(snowBoots)
    data = []
    for sboots in snowBoots:
        result = {}
        result["Brand"] = sboots.Brand
        result["Size"] = sboots.Size
        result["Availability"] = sboots.Availability
        data.append(result)
        print(data)
    return render(request=request,
                  template_name="Products/SnowboardBootsPage.html",
                  context={"data": data}
                  )