from django.shortcuts import render
from products.models import Product,Brand,Review
from django.db.models.aggregates import Count

def home(request):
    brands=Brand.objects.all()[:10].annotate(product_count=Count('product_brand'))
    sale_product=Product.objects.filter(flag='Sale')[:10]
    new_product=Product.objects.filter(flag='New')[:10]
    feature_product=Product.objects.filter(flag='Feature')[:6]

    reviews=Review.objects.all()


    context={
        'brands':brands,
        'sale_product':sale_product,
        'new_product':new_product,
        'feature_product':feature_product,
        'reviews':reviews
    }
    return render(request,'settings/home.html',context)
