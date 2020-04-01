from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from products.views import single_prod


@login_required
def view_cart(request):
    return render(request, "cart.html")


@login_required
def cart_add(request, id):
    q = int(request.POST.get('quantity'))
    s = request.POST.get('size')
    cart = request.session.get('cart', {})
    print(cart)

    if id in cart:
        print("id is in cart")
        if s in cart[id]:
            cart[id][s] = cart[id][s] + q
            print(cart[id])
        else:
            cart[id][s] = q  # lhs of new dict = rhs
    else:
        cart[id] = {s: q}
        print("id not in cart")

    # add another k/v pair to your cart id if size there
    # if the size is not already in the cart then you
    # want to add this new k/v pair onto this prod id

    request.session['cart'] = cart
    messages.success(request, "Item added to cart")
    return redirect(single_prod, id)


@login_required
def change_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('size')
    cart = request.session.get('cart', {})
    # print(cart[id])
    print(type(cart))
    print(cart)
    # print(cart[id][quantity])
    # print(cart[id][size])

    if quantity > 0:
        if size in cart[id]:
            cart[id][size] = quantity
            # print(cart[id])
        else:
            cart[id].pop(size)
            # cart[id][size] = quantity

            # cart[id][size] = cart[id].pop('size', quantity)
            # cart[id].update(cart[id])
            # cart[id][size] = quantity
            # print(cart[id])
    else:
        # cart[id].pop([id][quantity])
        cart[id].pop(size)
        # if else to pop out qunatity if size is 0

    request.session['cart'] = cart
    messages.success(request, "Cart updated")
    return redirect(reverse('view_cart'))
