from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    cart = request.session.get('cart', {})
    print(cart)

    cart_items = []
    prod_count = 0
    total = 0

    for id, content in cart.items():
        product = get_object_or_404(Product, pk=id)
        # quantity = content[]
        # # # size = content[1]
        # total += quantity * product.price
        for size, quantity in content.items():
            total += quantity * product.price
            prod_count += quantity
            cart_items.append({
                'id': id, 'quantity': quantity,
                'size': size, 'total': total, 'product': product
            })

    return {
        'cart_items': cart_items, 'total': total, 'product_count': prod_count
    }
