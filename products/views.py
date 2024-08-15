from django.shortcuts import render

from .models import Product,Brand,Review,ProductImage
from django.views.generic import ListView,DetailView

class Product_List(ListView):
    model=Product
    template_name='products/product_list.html'
    paginate_by=28


class Product_Detail(DetailView):
    model=Product
    template_name='products/product_detail.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object()).order_by('-id')[:3]
        context["images"] = ProductImage.objects.filter(product=self.get_object())
        context["related"] = Product.objects.filter(brand=self.get_object().brand)

        return context
    
