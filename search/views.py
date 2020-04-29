from django.shortcuts import render, redirect, reverse
from products.models import Product
import sweetify


# below code taken from a Code Institute tutorial and modified for my project
def search(request):
    """
    Searches product DB for string matches of names that match
    the query inputted by the user.
    """
    results = Product.objects.filter(name__icontains=request.GET['query'])
    if not results:
        sweetify.error(
            request,
            "No results for your search, try one of the below",
            icon='question',
            timer='3000',
            toast='true',
            position='top',
        )
        return redirect(reverse('products'))
    else:
        return render(request, "searchresults.html", {"products": results})
