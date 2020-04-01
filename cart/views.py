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
    print(s, q)
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

    # if id in cart:
    #     if size == cart[id][1]:  # if size equal to size there already in cart
    #         cart[id] = [int(cart[id][0]) + quantity, size]
    #         # adding the quantity added to
    #         # quantity integer there already
    #         print(cart[id])
    #     else:
    #         newid = [quantity, size]
    #         print(newid)
    #         print(cart[id])
    #         cart[id] = cart[id] + newid

    #         # add another k/v pair to your cart id if size there
    #         # if the size is not already in the cart then you
    #         # want to add this new k/v pair onto this prod id
    #         # if size = cart[id][1] else:
    #         # print(cart[id][0])
    #         # print(cart[id][1])
    #         print(cart[id])
    # else:
    #     cart[id] = cart.get(int(id), [quantity, size])
    #     print(cart[id])

    # if id in cart:
    #     # size = cart[id][1]
    #     if size in cart[id]:
    #         cart[id] = [int(cart[id][0]) + quantity, size]
    #         print(cart[id][size])
    #     else:
    #         cart[id] = [int(cart[id]) + quantity, size]
    #         # [int(cart[id][0]).update([(quantity, size)])]
    #         # cart[id] = cart[id].update({size: quantity for size, quantity in cart[id].iteritems() if quantity})
    #         print(cart[id])

    request.session['cart'] = cart
    messages.success(request, "Item added to cart")
    return redirect(single_prod, id)


@login_required
def change_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    size = request.POST.get('size')
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id][size] = quantity
    else:
        cart.pop(id[size])

    request.session['cart'] = cart
    messages.success(request, "Cart updated")
    return redirect(reverse('view_cart'))
