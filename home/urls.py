from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('<int:category_id>/', views.category, name='category'),
    path('<int:category_id>/<int:subcategory_id>/', views.subcategorypage, name='subcategory'),
    path('<int:category_id>/<int:subcategory_id>/<int:menu_id>/', views.menupage, name='menu'),
    path('product/<int:product_id>/', views.singleproduct, name='product'),
    path('login/', views.login_view, name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('search/',views.search,name='search')
]