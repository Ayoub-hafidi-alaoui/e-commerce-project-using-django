from unicodedata import name
from django.urls import path
from .views import BrandDetail, BrandList, CategoryList, ProductList, ProductDetail, post_list

app_name = "products"

urlpatterns = [
    path('test/', post_list, name="testing"),
    path('', ProductList.as_view(), name="products_list"),
    path('<int:pk>', ProductDetail.as_view(), name="products_details"),
    path('brands/', BrandList.as_view(), name="brand_list"),
    path('brands/<int:pk>', BrandDetail.as_view(), name="brand_detail"),
    path('categories/', CategoryList.as_view(), name="category_list")
    
]