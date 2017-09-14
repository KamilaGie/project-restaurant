from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import *
from django.template import Template, Context

from django.contrib.auth import authenticate, login, logout



class HomeView(View):

    def get(self, request):
        category = Category.objects.all()
        return render(request, "home.html", {"category":category})



class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'message': '', 'form':form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('login')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                if user.groups.filter(name="Kelnerzy"):
                    return redirect('home')
                if user.groups.filter(name="Barmani"):
                    return redirect('bar')
                if user.groups.filter(name="Kucharze"):
                    return redirect('kitchen')
                return redirect('home')
            else:
                message = 'Błędny login lub hasło'
                return render(request, 'login.html', {'message': message, 'form':form})
        else:
            return render(request, 'login.html', {'message': '', 'form':form})

def LogoutView(request):

    if request.user.is_authenticated:
        user = request.user
        logout(request)
        return redirect('login')
    else:
        return HttpResponse('Najpierw należy się zalogować!')


class CategoryView(View):

    def get(self, request, c):
        category = Category.objects.get(name = c)
        products = category.product_set.all()

        return render(request, "base.html", {"c": c, "category": category, "products": products})


class OrderView(View):

    def get(self, request, c, p):
        category = Category.objects.get(name = c)
        products = category.product_set.all()
        form = OrderForm()
        return render(request, 'order.html', {"c": c, "form":form, "category": category, "products": products })

    def post(self, request, c, p):
        category = Category.objects.get(name = c)
        products = category.product_set.get(name = p)
        kitchen = ('Galletes', 'Crepes', 'Pancakes', 'Salads')
        bar = ('SoftDrinks', 'Alcohols')
        id = products.id
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                description = form.cleaned_data['description']
                quantity = form.cleaned_data['quantity']
                Order.objects.create(description=description, quantity=quantity, product_id=id)
                if c in kitchen:
                    return HttpResponse("Success kitchen")
                elif c in bar:
                    return HttpResponse("Success bar")
            else:
                return HttpResponse("coś poszlo nie tak")

class KitchenView(View):
    def get(self, request):
        order = Order.objects.filter(product_id__lte=29)
        return render(request, "kitchen.html", {"order":order})



class BarView(View):
    def get(self, request):
        order = Order.objects.filter(product_id__gt=29)
        return render(request, "bar.html", {"order":order})




