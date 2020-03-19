from django.shortcuts import render, redirect, reverse
from products.models import Product
from django.contrib import messages


def search(request):
    results = Product.objects.filter(name__icontains=request.GET['query'])
    if not results:
        messages.error(request, "no results for your search")
        return redirect(reverse('products'))
    else:
        return render(request, "products.html", {"products": results})


def cat_search(request):
    results = Product.objects.filter(category__icontains=request.GET['cats'])
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