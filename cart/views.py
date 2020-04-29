from django.shortcuts import render, redirect, reverse
from products.views import single_prod
import sweetify


def view_cart(request):
    """Returns the user's shopping cart"""
    return render(request, "cart.html")


# below code taken from a Code Institute tutorial intially and
# were modified heavily to suit the needs of my project
def cart_add(request, id):
    """
    Add another k/v pair to your cart id if size there
    if the size is not already in the cart then you
    want to add this new k/v pair onto this prod id
    dict / cart dict. Checks category to make sure
    same plan isn't added twice. Add sweetify alert
    depending on the transaction.
    """
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
            cart[id][s] = q
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

    request.session['cart'] = cart
    return redirect(single_prod, id)


# below code taken from a Code Institute tutorial intially and
# were modified heavily to suit the needs of my project
def change_cart(request, id):
    """
    Alter items in cart, if previous size is same
    then quantity is what user selects, if oldsize
    and new size are different, pop the old size kv,
    new kv entry for this prod is now what the
    user selected. Add sweetify alert saying item
    updated.
    """
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('size')
    oldsize = request.POST.get('oldsize')
    cart = request.session.get('cart', {})

    if size == oldsize:
        cart[id][size] = quantity
    else:
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
    """
    Remove item form cart, check for an empty
    dict for this id delete it if so. Add sweetify
    alert.
    """
    size = request.POST.get('sizez')
    cart = request.session.get('cart', {})

    cart[id].pop(size)
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
