from django.urls import path
from .views import Product_Detail,Product_List,add_review,Brand_List,Brand_Detail

urlpatterns = [
    path('',Product_List.as_view()),
    path('brands/<slug:slug>',Brand_Detail.as_view()),

    path('brands',Brand_List.as_view()),

    path('add_review/<slug:slug>',add_review),
    path('<slug:slug>',Product_Detail.as_view()),

]
