from django.shortcuts import render,redirect

from .models import Product,Brand,Review,ProductImage
from django.views.generic import ListView,DetailView

from django.db.models.aggregates import Count

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


def add_review(request,slug):

    user=request.user
    product=Product.objects.get(slug=slug)
    rate=request.POST['rating']
    review=request.POST['review']

    Review.objects.create(
        user=user,
        product=product,
        rate=rate,
        review=review
    )
    return redirect(f'/products/{slug}')

class Brand_List(ListView):
    model=Brand
    template_name='products/brands_list.html'
    paginate_by=25

    queryset=Brand.objects.annotate(product_count=Count('product_brand'))

# class Brand_Detail(DetailView):
#     model=Brand
#     template_name='products/brand_detail.html'

#     def get_context_data(self, **kwargs) :
#         context = super().get_context_data(**kwargs)
#         context["related"] = Product.objects.filter(brand=self.get_object()) 
#         return context
    
class Brand_Detail(ListView):
    model=Product
    template_name='products/brand_detail.html'
    paginate_by=5

    def get_queryset(self):
        brand=Brand.objects.get(slug=self.kwargs['slug'])
        queryset= super().get_queryset().filter(brand=brand)
        return queryset
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
        return context
    
    

   
    
    

    
