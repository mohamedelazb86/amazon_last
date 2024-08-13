from django.urls import path
from .views import post_list,post_detail,create_post,update_post,delete_post

urlpatterns = [
    path('',post_list),
    path('create_post',create_post),
    path('<slug:slug>',post_detail),
    path('update_post/<slug:slug>',update_post),
    path('delete_post/<slug:slug>',delete_post)

]
