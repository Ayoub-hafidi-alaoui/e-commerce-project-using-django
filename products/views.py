from unicodedata import category
from django.views.generic import ListView, DetailView
from django.shortcuts import render

from .models import Category, Product, ProductImages, Brand
from django.db.models import Count, Q, F



def post_list(request):
    #products = Product.objects.filter(price__range=(30, 50))
    #products = Product.objects.filter(name__endswith='ay')
    products = Product.objects.all()
    return render(request, "products/test_list.html", {"products":products})


class ProductList(ListView):
    model = Product
    paginate_by = 400
    
    
class ProductDetail(DetailView):
    model=Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myProduct = self.get_object()
        context["images"] =  ProductImages.objects.filter(product=myProduct)
        context["related"] = Product.objects.filter(category=myProduct.category)
        return context
    
class BrandList(ListView):
    model = Brand
    paginate_by = 20
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.all().annotate(product_count=Count("product_brand"))
        return context
    

class BrandDetail(DetailView):
    model = Brand
    paginate_by = 10
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        brand = self.get_object()
        context["brand_products"] = Product.objects.filter(brand=brand)
        return context
    


class CategoryList(ListView):
    model = Category
    paginate_by = 10
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all().annotate(product_count=Count("product_category"))
        return context
