from django.shortcuts import render, redirect, reverse
from .models import Product
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def all_prods(request):
    products = Product.objects.all().order_by('-price')
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 1)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, "products.html", {"products": products})


def apparel(request):
    results = Product.objects.filter(category__icontains='apparel')
    if not results:
        messages.error(request, "no results for your search")
        return redirect(reverse('products'))
    else:
        return render(request, "prods-apparel.html", {"products": results})


def plans(request):
    results = Product.objects.filter(category__icontains='plan')
    if not results:
        messages.error(request, "no results for your search")
        return redirect(reverse('products'))
    else:
        return render(request, "prods-plans.html", {"products": results})


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


def sort_apparel(request):
    select = request.GET['sorta']
    items = Product.objects.filter(category__icontains='apparel')
    if select == 'LtoH':
        results = items.order_by('price')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "prods-apparel.html", {"products": results})
    elif select == 'HtoL':
        results = items.order_by('-price')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "prods-apparel.html", {"products": results})


def sort_plans(request):
    select = request.GET['sortp']
    items = Product.objects.filter(category__icontains='plan')
    if select == 'LtoH':
        results = items.order_by('price')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "prods-plans.html", {"products": results})
    elif select == 'HtoL':
        results = items.order_by('-price')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "prods-plans.html", {"products": results})
