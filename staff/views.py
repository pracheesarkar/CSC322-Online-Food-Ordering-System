from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import datetime
from customer.models import *
from django.views.decorators.http import require_http_methods
import json
from django.http import HttpResponse, JsonResponse
from django.db import connection, transaction
from allauth.account.forms import LoginForm, SignupForm

import json
from django.http import HttpResponse, JsonResponse
from .models import Employee
from .forms import *

# Create your views here.

def addfood(request):
    if request.method == "POST":
        form = Menuform(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get("name")
            price = form.cleaned_data.get("price")
            category = form.cleaned_data.get("category")
            image = form.cleaned_data.get("image")
            obj = MenuItem.objects.create(
                name = name,
                price = price,
                image = image
            )
            obj.category.add(category)
            obj.save()
            return redirect("/order")
        
    else:
        form = Menuform()
    return render(request,'staff/addfood.html',{'form':form})

class AddFood (View):
    model = MenuItem
    form_class = Menuform
    template_name = 'staff/addfood.html'
    
    
    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()
    
            
class Dashboard(View):
    def get(self, request, *args, **kwargs):
        # get the current date
        today = datetime.today()
        orders = OrderModel.objects.filter(
            created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)

        # loop through the orders and add the price value
        total_revenue = 0
        for order in orders:
            total_revenue += order.price

        # pass total number of orders and total revenue into template
        context = {
            'orders': orders,
            'total_revenue': total_revenue,
            'total_orders': len(orders)
        }

        return render(request, 'staff/dashboard.html', context)
    
    def test_func(self):
        return self.request.user.groups.filter(name='Chef').exists()

    
class Deliver(View):
    def get(self, request, *args, **kwargs):
        # get the current date
        today = datetime.today()
        orders = OrderModel.objects.filter(
            created_on__year=today.year, created_on__month=today.month, created_on__day=today.day)

        # loop through the orders and add the price value
        total_revenue = 0
        for order in orders:
            total_revenue += order.price

        # pass total number of orders and total revenue into template
        context = {
            'orders': orders,
            'total_revenue': total_revenue,
            'total_orders': len(orders)
        }

        return render(request, 'staff/deliver.html', context)

    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()
    
    '''
    def addfood(request):
       if request.method == "POST":
              form = Menuform(request.POST)
              if form.is_valid():
                form.save()
                return redirect("/order")
       else:
              form = Menuform()
       return render(request,'staff/addfood.html',{'form':form})


       <div class="form-group form-check">
                    <input type="checkbox" name="Cakes" class="form-check-input" value="Cakes">
                    <label class="form-check-label">Cakes</label>
                </div>
                <div class="form-group form-check">
                    <input type="checkbox" name="Cookies" class="form-check-input" value="Cookies">
                    <label class="form-check-label">Cookies</label>
                </div>


                class Dashboard(View):
    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()
       '''