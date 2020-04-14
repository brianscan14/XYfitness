from django.shortcuts import render, redirect, reverse
from products.models import Product
from django.contrib import messages


def search(request):
    results = Product.objects.filter(name__icontains=request.GET['query'])
    if not results:
        messages.error(request, "no results, see if anything matches below")
        return redirect(reverse('products'))
    else:
        return render(request, "searchresults.html", {"products": results})
