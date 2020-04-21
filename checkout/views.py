from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
import stripe
import sweetify
import random


stripe.api_key = settings.STRIPE_SECRET


@login_required()
def delivery(request):
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            request.session['delivery_data'] = order_form.cleaned_data
            cart = request.session.get('cart', {})
            total = 0
            del_total = 0

            for id, content in cart.items():
                product = get_object_or_404(Product, pk=id)
                cat = Product.objects.filter(id=id, category__icontains='A')
                if cat:
                    del_total = 5
                for size, quantity in content.items():
                    total += quantity * product.price

            total = del_total + total
            return redirect('checkout')
    else:

        if request.session.get('delivery_data'):
            order_form = OrderForm(initial=request.session['delivery_data'])
        else:
            order_form = OrderForm()

    return render(request, "deliver.html", {"order_form": order_form})


@login_required()
def checkout(request):
    delivery_details = request.session['delivery_data']
    order_form = OrderForm(delivery_details)
    if request.method == "POST":
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            del_total = 0

            for id, content in cart.items():
                product = get_object_or_404(Product, pk=id)
                cat = Product.objects.filter(id=id, category__icontains='A')
                if cat:
                    del_total = 5
                for size, quantity in content.items():
                    total += quantity * product.price
                    order_line_item = OrderLineItem(
                        order=order,
                        product=product,
                        quantity=quantity,
                    )
                    order_line_item.save()
            total = del_total + total
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                sweetify.error(
                    request,
                    "Your card was declined!",
                    icon='error',
                    timer='1500',
                    toast='true',
                    position='center',
                )

            if customer.paid:
                request.session['cart'] = {}

                order_no = random.randint(1, 10000)
                title = 'Thank you for order at XY, ' + request.user.username
                email = request.user.email
                message = 'Your order number is: ' + str(order_no) \
                        + ', Thank you for using our website, ' \
                        + 'Total = €' + str(total)
                try:
                    send_mail(title, message, email, ['admin@hotmail.com'])
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')

                return redirect('order_confirm')

            else:
                sweetify.error(
                    request,
                    "Unable to take payment",
                    icon='error',
                    timer='2000',
                    toast='true',
                    position='center',
                )
        else:
            print(payment_form.errors)
            sweetify.error(
                request,
                "Unable to take a payment with that card!",
                icon='error',
                timer='1500',
                toast='true',
                position='center',
            )
    else:
        payment_form = MakePaymentForm()

    name = request.session['delivery_data']['full_name']
    address = request.session['delivery_data']['street_address2']
    town = request.session['delivery_data']['town_or_city']
    county = request.session['delivery_data']['county']

    return render(request, "checkout.html", {
        "order_form": order_form,
        "payment_form": payment_form,
        "name": name,
        "address": address,
        "town": town,
        "county": county,
        "publishable": settings.STRIPE_PUBLISHABLE
        })

@login_required()
def order_confirm(request):
    return render(request, "order-confirmed.html")
