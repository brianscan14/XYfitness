from django.shortcuts import render, redirect, reverse
from products.views import single_prod
import sweetify


def view_cart(request):
    return render(request, "cart.html")


def cart_add(request, id):
    q = int(request.POST.get('quantity'))
    s = request.POST.get('size')
    category = request.POST.get('category')
    cart = request.session.get('cart', {})

    if id in cart:
        if category == 'plan':
            sweetify.success(
                request,
                "Plan in cart already, can't add again!",
                icon='info',
                timer='3000',
                toast='true',
                position='top-end',
            )
        elif s in cart[id]:
            cart[id][s] = cart[id][s] + q
            sweetify.success(
                request,
                "Cart updated",
                icon='success',
                timer='3000',
                toast='true',
                position='top-end',
            )
        else:
            cart[id][s] = q  # lhs of new dict = rhs
            sweetify.success(
                request,
                "Item added to cart",
                icon='success',
                timer='1500',
                toast='true',
                position='center',
                background='#181818',
            )
    else:
        cart[id] = {s: q}
        sweetify.success(
            request,
            "Item added to cart",
            icon='success',
            timer='1500',
            toast='true',
            position='center',
            background='#181818',
        )

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
    sweetify.success(
        request,
        "Item updated",
        icon='success',
        timer='2500',
        toast='true',
        position='top-end',
    )
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
    sweetify.success(
        request,
        "Item removed",
        icon='success',
        timer='3000',
        toast='true',
        position='top-end',
    )
    return redirect(reverse('view_cart'))
