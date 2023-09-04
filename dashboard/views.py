from django.shortcuts import render, redirect
from cart import models
from home.models import product
from django.contrib.auth.decorators import login_required
import datetime
from django.db.models import Sum, F

# Create your views here.


@login_required
def dashboard(request):
    return render(request, 'layout/dashboard.html')


@login_required
def orders(request):
    orders = models.order.objects.all().order_by('-created_at')
    carts = models.cart.objects.all()
    orderItems = models.orderItem.objects.all()

    context = {
        'orders':orders,
        'carts':carts,
        'orderItem':orderItems
    }

    return render(request,'orders.html', context)


@login_required
def sinleOrder(request, order_id):
    order = models.order.objects.get(id=order_id)
    order_items = models.orderItem.objects.filter(order=order)
    orderTotal = models.orderItem.objects.filter(order=order).aggregate(
        total=Sum(F('variant__price') * F("quantity"))
    )

    context = {
        "order": order,
        "orderItems": order_items,
        'orderTotal':orderTotal
    }

    return render(request, 'singleOrder.html', context)


@login_required
def delete(request,order_id):
    order = models.order.objects.get(id=order_id)
    order.delete()
    return redirect('orders')


@login_required
def products(request):
    products = product.objects.all()
    return render(request,'dashproducts.html', {'products':products})


@login_required
def deleteproduct(request, product_id):
    Product = product.objects.get(id=product_id)
    Product.delete()
    return redirect('productsdash')


@login_required
def addproduct(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        des = request.POST['des']
        image = request.FILES['image']

        product.objects.create(name=name,price=float(price),description=des, image=image)
    return render(request,'addproduct.html')


@login_required
def edit(request,product_id):
    products = product.objects.get(id=product_id)
    if request.method == 'POST':
        products.name = request.POST['name']
        products.price = request.POST['price']
        products.description = request.POST['des']
        products.image = request.FILES['image']

        products.save()
    return render(request,'edit.html',{'product':products})


@login_required
def customers(request):
    customers = models.customer.objects.all().order_by('-created_at')
    return render(request,'customers.html', {"customers": customers})


@login_required
def reports(request):
    # creating days variables
    today = datetime.datetime.today().date()
    last_week = today - datetime.timedelta(days=7)
    last_month = today - datetime.timedelta(days=30)
    last_threeMoths = today - datetime.timedelta(days=90)

    # get the total number of orders for different time periods
    daily_orders = models.order.objects.filter(created_at__gte=today).count()
    orders_week = models.order.objects.filter(created_at__gte=last_week).count()
    orders_month = models.order.objects.filter(created_at__gte=last_month).count()
    orders_three =  models.order.objects.filter(created_at__gte=last_threeMoths).count()

    # getting the revenue
    daily_revenue = models.orderItem.objects.filter(order__created_at__gte=today).aggregate(
        revenue=Sum(F('variant__price') * F("quantity"))
    )
    revenue_week = models.orderItem.objects.filter(order__created_at__gte=last_week).aggregate(
        revenue=Sum(F('variant__price') * F('quantity')))
    revenue_month = models.orderItem.objects.filter(order__created_at__gte=last_month).aggregate(
        revenue=Sum(F('variant__price') * F('quantity')))
    revenue_three = models.orderItem.objects.filter(order__created_at__gte=last_threeMoths).aggregate(
        revenue=Sum(F('variant__price') * F('quantity')))

    # number of items have been sold
    items_sold = models.orderItem.objects.all().aggregate(number=Sum(F('quantity')))

    context = {
        'daily_orders': daily_orders,
        'last_week_orders': orders_week,
        'last_month_orders': orders_month,
        'last_3months_orders': orders_three,
        'daily_revenue': daily_revenue,
        'last_week_revenue': revenue_week,
        'last_month_revenue': revenue_month,
        'last_3months_revenue': revenue_three,
        'items_sold': items_sold,
    }
    return render(request, 'reports.html', context)

# Create your views here.
