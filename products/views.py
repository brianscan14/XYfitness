from django.shortcuts import render, redirect, reverse
from .models import Product
from django.contrib import messages


# Create your views here.
def all_prods(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def apparel(request):
    results = Product.objects.filter(category__icontains='apparel')
    if not results:
        messages.error(request, "no results for your search")
        return redirect(reverse('products'))
    else:
        return render(request, "products.html", {"products": results})


def plans(request):
    results = Product.objects.filter(category__icontains='plan')
    if not results:
        messages.error(request, "no results for your search")
        return redirect(reverse('products'))
    else:
        return render(request, "products.html", {"products": results})


def sort(request):
    select = request.GET['sort']
    if select == 'LtoH':
        results = Product.objects.order_by('price')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "products.html", {"products": results})
    elif select == 'HtoL':
        results = Product.objects.order_by('-price')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "products.html", {"products": results})


def test(request):
    select = request.GET['sort']
    if request.get_full_path == '/products/':
        results = Product.objects.order_by('price')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "products.html", {"products": results})