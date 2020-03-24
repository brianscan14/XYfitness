from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Product, ProductReview
from django.contrib import messages
from .forms import ProdReviewForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


def all_prods(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def single_prod(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'aproduct.html', {'product': product})


@login_required()
def review_prod(request, pk):
    product = get_object_or_404(Product, pk=pk)
    user = request.user
    if request.method == "POST":
        if ProductReview.objects.filter(user=user, product=product).exists():
            # old_review = ProductReview.objects.filter(user=user, product=product)
            form = ProdReviewForm(request.POST)
            messages.error(request, "Already reviewed this product!")
            return redirect(single_prod, product.pk)
        else:
            form = ProdReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.product = product
                form.instance.user = request.user
                review.save()
                messages.success(request, "Review Added")
                return redirect(single_prod, product.pk)
    else:
        form = ProdReviewForm()
    return render(request, 'prodreview.html', {'form': form})


@login_required()
def edit_review_prod(request, pk):
    review = get_object_or_404(ProductReview, pk=pk)
    product = review.product_id
    if request.method == "POST":
        form = ProdReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            form.instance.user = request.user
            review.save()
            messages.success(request, "Review updated")
            return redirect(single_prod, product)
    else:
        form = ProdReviewForm(instance=review)
    return render(request, 'editprodreview.html', {'form': form})


@login_required()
def delete_prod_review(request, pk):
    review = get_object_or_404(ProductReview, pk=pk)
    if review.user == request.user:
        review.delete()
        messages.success(request, "Your review was deleted")
        return redirect(all_prods)


def apparel(request):
    results = Product.objects.filter(category__icontains='A')
    if not results:
        messages.error(request, "no results for your search")
        return redirect(reverse('products'))
    else:
        return render(request, "prods-apparel.html", {"products": results})


def plans(request):
    results = Product.objects.filter(category__icontains='P')
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
    elif select == 'AtoZ':
        results = Product.objects.order_by('name')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "products.html", {"products": results})
    elif select == 'ZtoA':
        results = Product.objects.order_by('-name')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "products.html", {"products": results})


def sort_apparel(request):
    select = request.GET['sorta']
    items = Product.objects.filter(category__icontains='A')
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
    elif select == 'AtoZ':
        results = items.order_by('name')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "prods-apparel.html", {"products": results})
    elif select == 'ZtoA':
        results = items.order_by('-name')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "prods-apparel.html", {"products": results})


def sort_plans(request):
    select = request.GET['sortp']
    items = Product.objects.filter(category__icontains='P')
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
    elif select == 'AtoZ':
        results = items.order_by('name')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "prods-plans.html", {"products": results})
    elif select == 'ZtoA':
        results = items.order_by('-name')
        if not results:
            messages.error(request, "no results for your search")
            return redirect(reverse('products'))
        else:
            return render(request, "prods-plans.html", {"products": results})
