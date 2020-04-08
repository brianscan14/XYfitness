from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.views import single_prod


def view_cart(request):
    return render(request, "cart.html")


def cart_add(request, id):
    q = int(request.POST.get('quantity'))
    s = request.POST.get('size')
    category = request.POST.get('category')
    cart = request.session.get('cart', {})

    if id in cart:
        if category == 'plan':
            messages.error(request, "Plan in cart already")
        elif s in cart[id]:
            cart[id][s] = cart[id][s] + q
            messages.success(request, "Cart updated")
        else:
            cart[id][s] = q  # lhs of new dict = rhs
            messages.success(request, "Item added to cart")
    else:
        cart[id] = {s: q}
        messages.success(request, "Item added to cart")

    # add another k/v pair to your cart id if size there
    # if the size is not already in the cart then you
    # want to add this new k/v pair onto this prod id

    request.session['cart'] = cart
    return redirect(single_prod, id)


def change_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('size')
    oldsize = request.POST.get('oldsize')
    cart = request.session.get('cart', {})

    if size == oldsize:
        # if previosu size is same then quantity is what user selects
        cart[id][size] = quantity
    else:
        # if oldsize and new size are different, pop the old size kv
        # kv entry for this prod is now what the user selected
        cart[id].pop(oldsize)
        cart[id][size] = quantity

    request.session['cart'] = cart
    messages.success(request, "Cart updated")
    return redirect(reverse('view_cart'))


def del_cart_item(request, id):
    size = request.POST.get('sizez')
    cart = request.session.get('cart', {})

    cart[id].pop(size)
    # check for an empty dict for this id
    # delete it if so
    if len(cart[id]) == 0:
        del cart[id]

    request.session['cart'] = cart
    messages.success(request, "Item removed")
    return redirect(reverse('view_cart'))
