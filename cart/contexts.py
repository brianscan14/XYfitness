from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    cart = request.session.get('cart', {})
    cart_items = []
    prod_count = 0
    total = 0
    del_total = 0

    for id, content in cart.items():
        product = get_object_or_404(Product, pk=id)
        print(product.category)
        cat = Product.objects.filter(id=id, category__icontains='A')
        if cat:
            del_total = 5
        else:
            del_total = 0
        print(del_total)
        for size, quantity in content.items():
            this_total = quantity * product.price
            total += quantity * product.price
            prod_count += quantity
            cart_items.append({
                'id': id, 'quantity': quantity, 'this_total': this_total,
                'size': size, 'total': total, 'product': product
            })

    subtotal = total
    print(subtotal)
    total = del_total + total
    print(total)

    return {
        'cart_items': cart_items,
        'total': total,
        'subtotal': subtotal,
        'del_total': del_total,
        'product_count': prod_count
    }
