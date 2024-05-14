import json
from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from .models import *
from .forms import *
from allauth.account.views import SignupView
#from allauth import SignupView
import os
from onlinebakery.settings import BASE_DIR
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin


             
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')


class Order(View):
    def get(self, request, *args, **kwargs):
        # get every item from each category
        cakes = MenuItem.objects.filter(
            category__name__contains='Cakes')
        cookies = MenuItem.objects.filter(category__name__contains='Cookies')
        

        # pass into context
        context = {
            'cakes': cakes,
            'cookies': cookies,
        }

        # render the template
        return render(request, 'customer/order.html', context)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')


        order_items = {
            'items': []
        }

        items = request.POST.getlist('items[]')

        for item in items:
            menu_item = MenuItem.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data)

            price = 0
            item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(
            price=price,
            name=name,
            email=email,
            address=address
        )
        order.items.add(*item_ids)

        # After everything is done, send confirmation email to the user
        body = ('Thank you for your order! Your food is being made and will be delivered soon!\n'
                f'Your total: {price}\n'
                'Thank you again for your order!')

        send_mail(
            'Thank You For Your Order!',
            body,
            'example@example.com',
            [email],
            fail_silently=False
        )

        context = {
            'items': order_items['items'],
            'price': price
        }

        return redirect('order-confirmation', pk=order.pk)


class OrderConfirmation(View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        context = {
            'pk': order.pk,
            'items': order.items,
            'price': order.price,
        }

        return render(request, 'customer/order_confirmation.html', context)

    def post(self, request, pk, *args, **kwargs):
        data = json.loads(request.body)

        if data['isPaid']:
            order = OrderModel.objects.get(pk=pk)
            order.is_paid = True
            order.save()

        return redirect('payment-confirmation')


class OrderPayConfirmation(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/order_pay_confirmation.html')
    

class Menu(View):
    def get(self, request, *args, **kwargs):
        menu_items = MenuItem.objects.all()

        context = {
            'menu_items': menu_items
        }

        return render(request, 'customer/menu.html', context)
    
def reviews(request):
    if request.method == "POST":
        form = Reviewform(request.POST)
        if form.is_valid():
            form.save()
            #return redirect("/reviews")
    else:
        form = Reviewform()
    return render(request,'customer/review.html',{'form':form})

class ViewReview(View):
    def get(self, request):
        reviews = ReviewModel.objects.all()

        context = {
            'reviews': reviews
        }

        return render(request, 'customer/view_reviews.html', context)


'''

def view_reviews(request):
    return render(request, 'customer/view_reviews.html')

class ViewReview(View):
    def get(self, request, pk, *args, **kwargs):
        order = ReviewModel.objects.all()

        context = {
            'name': order.name,
            'email': order.email,
            'review': order.review,
        }

        return render(request, 'customer/view_reviews.html', context)
'''