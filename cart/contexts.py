from django.shortcuts import get_object_or_404
from products.models import Product


# below code taken from a Code Institute tutorial intially and
# were modified to suit the needs of my project
def cart_contents(request):
    """
    Iterates through the dict items in the cart and returns value for
    each product's dict k/v pair. Also adds delivery total to monetary
    cost of items if there ia an apparel item in the bag.
    """
    cart = request.session.get('cart', {})
    cart_items = []
    prod_count = 0
    total = 0
    del_total = 0

    for id, content in cart.items():
        product = get_object_or_404(Product, pk=id)
        cat = Product.objects.filter(id=id, category__icontains='A')
        if cat:
            del_total = 5
        for size, quantity in content.items():
            this_total = quantity * product.price
            total += quantity * product.price
            prod_count += quantity
            cart_items.append({
                'id': id, 'quantity': quantity, 'this_total': this_total,
                'size': size, 'total': total, 'product': product
            })

    subtotal = total
    total = del_total + total

    return {
        'cart_items': cart_items,
        'total': total,
        'subtotal': subtotal,
        'del_total': del_total,
        'product_count': prod_count
    }
