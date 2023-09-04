from django.shortcuts import render, HttpResponse,redirect
from . import models
from django.db.models import Min, Max
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    all = models.product.objects.all()[:4]
    skin = models.product.objects.filter(category=1)[:4]
    context = {
        'all': all,
        'skin': skin,
    }
    return render(request, "home.html", context)


def category(request, category_id):
    category = models.Category.objects.get(id=category_id)
    product = models.product.objects.filter(category=category)
    context = {
        'category': category,
        'product': product
    }
    return render(request,'category.html',context)


def subcategorypage(request, category_id, subcategory_id):
    category = models.Category.objects.get(id=category_id)
    subcategory = models.SubCategory.objects.get(id=subcategory_id)
    products = models.product.objects.filter(category=category, subCategory=subcategory)

    context = {
        'products': products,
        'sub': subcategory,
    }

    return render(request, 'sub.html', context)


def menupage(request, category_id, subcategory_id, menu_id):
    category = models.Category.objects.get(id=category_id)
    subcategory = models.SubCategory.objects.get(id=subcategory_id)
    menu = models.MenuItems.objects.get(id=menu_id, subCategory=subcategory)
    products = models.product.objects.filter(category=category, subCategory=subcategory, menuitem=menu)

    context = {
        'products': products,
        'menu': menu
    }
    return render(request, 'menu.html', context)


def singleproduct(request, product_id):
    product = models.product.objects.get(id=product_id)
    sub_categories = product.subCategory.all()
    sub_category_names = [subcategory.name for subcategory in sub_categories]
    variants = models.ProductVariant.objects.filter(product=product)
    # calculating the price range
    price_range = variants.aggregate(min_price=Min('price'), max_price=Max('price'))
    min_price = price_range['min_price']
    max_price = price_range['max_price']
    related = models.product.objects.filter(subCategory__name__in=sub_category_names)[:4]
    context = {
        'product': product,
        'variants': variants,
        'sub': sub_categories,
        'related': related,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'product.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            print('error')
    return render(request,'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def search(request):
    query = request.GET.get('query')
    results = models.product.objects.filter(name__icontains=query)
    context = {
        'result':results
    }

    return render(request,'result.html',context)
