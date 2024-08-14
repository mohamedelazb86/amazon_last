from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Product,Review,Brand,ProductImage

class ProductImagestub(admin.TabularInline):
    model=ProductImage

class ProductAdmin(SummernoteModelAdmin):
    list_display=['name','price','sku']
    list_filter=['brand']
    search_fields=['name','subtitle','descriptions']

    summernote_fields = ('subtitle','descriptions')
    
    inlines=[ProductImagestub]



admin.site.register(Product,ProductAdmin)
admin.site.register(Review)
admin.site.register(Brand)
#admin.site.register(ProductImage)
