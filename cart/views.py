from django.shortcuts import render, HttpResponse, redirect
from home import models
from . import models
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_to_cart(request, product_id):
    product = models.product.objects.get(id=product_id)
    variant_id = request.POST.get('variant')
    quantity = request.POST.get('quantity', 1)

    # Create or get the cart
    cart_id = _cart_id(request)
    cart, _ = models.cart.objects.get_or_create(cart_id=cart_id)

    if product.variants.count() > 1:
        # Product has multiple variants
        variant = models.ProductVariant.objects.get(id=variant_id)
        cart_item, created = models.cartItem.objects.get_or_create(cart=cart, product=product, variant=variant)
        cart_item.quantity += int(quantity)
        cart_item.save()
    else:
        # Product has only one variant
        default_variant = product.variants.first()
        cart_item, created = models.cartItem.objects.get_or_create(cart=cart, product=product, variant=default_variant)
        cart_item.quantity += int(quantity)
        cart_item.save()

    return redirect('cart')


def remove(request, product_id, variant_id):
    product = models.product.objects.get(id=product_id)
    cart = models.cart.objects.get(cart_id=_cart_id(request))
    cart_item = models.cartItem.objects.get(product=product, cart=cart, variant=variant_id)
    if cart_item.quantity >= 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')


def delete(request,product_id):
    product = models.product.objects.get(id=product_id)
    cart = models.cart.objects.get(cart_id=_cart_id(request))
    cart_item = models.cartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart')


def cart(request, total=0, quantity=0, cart_items=None):
    try:
        cart = models.cart.objects.get(cart_id=_cart_id(request))
        cart_items = models.cartItem.objects.filter(cart=cart, is_active=True)
        for item in cart_items:
            total += (item.variant.price * item.quantity)
            quantity += item.quantity
    except ObjectDoesNotExist:
        pass
    grandTotal = total + 3
    context = {
        "quantity": quantity,
        'total': total,
        "cart_items": cart_items,
        'grandTotal': grandTotal

    }
    return render(request, 'cart.html', context)


def checkout(request):
    cart = models.cart.objects.get(cart_id=_cart_id(request))
    cart_items = models.cartItem.objects.filter(cart=cart)
    # getting the deta from the form
    if request.method == 'POST':
        firstName = request.POST['fName']
        lastName = request.POST['lName']
        Phone = request.POST['phone']
        Shipping = request.POST['shipping']

        # create a new order and new customer
        Customer = models.customer.objects.get_or_create(name=f"{firstName} {lastName}", phone=Phone, address=Shipping)
        order = models.order.objects.create(fName=firstName, lName=lastName, phone=Phone, shipping=Shipping, cart=cart)

        # Assign each cart item to the order
        for cart_item in cart_items:
            models.orderItem.objects.create(order=order, product=cart_item.product, variant=cart_item.variant, quantity=cart_item.quantity)
        cart_items.delete()
        return redirect('home')
    return render(request, 'checkout.html')
