from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='addtocart'),
    path('', views.cart, name='cart'),
    path('remove/<int:product_id>/<int:variant_id>', views.remove, name='remove'),
    path('delete/<int:product_id>',views.delete,name='delete'),
    path('checkout/',views.checkout,name='checkout'),
]
