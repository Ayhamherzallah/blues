from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('orders/', views.orders, name='orders'),
    path('orders/<int:order_id>', views.sinleOrder, name='singleorder'),
    path('orders/delete/<int:order_id>', views.delete, name='deleteOrder'),
    path('products/', views.products, name='productsdash'),
    path('products/delete/<int:product_id>/', views.deleteproduct, name='deleteProduct'),
    path('product/add/', views.addproduct, name='addproduct'),
    path('product/edit/<int:product_id>/', views.edit, name='edit'),
    path('customers/', views.customers, name='customers'),
    path('reports/', views.reports, name='reports')
]