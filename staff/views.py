from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.utils.timezone import datetime
from customer.models import *
from django.views.decorators.http import require_http_methods

# Create your views here.

class AddFood (LoginRequiredMixin, UserPassesTestMixin, View):
    @require_http_methods(["GET", "POST"])
    def new_item(self, request, name, price, category):
        item = MenuItem.objects.create()
        item.name = name
        item.price = price
        item.category = category
        item.save()

        context = {
            'name': name,
            'price': price,
            'category': len(category)
        }

        return render(request, 'staff/addfood.html', context)
    
    def test_func(self):
        return self.request.user.groups.filter(name='Staff').exists()

class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
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
        return self.request.user.groups.filter(name='Staff').exists()