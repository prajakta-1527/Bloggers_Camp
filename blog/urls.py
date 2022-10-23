from django.contrib import admin
from django.urls import path, include
from blog import views
urlpatterns = [
   
    path('', views.blog, name='blog'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('addblogs', views.addblogs, name='addblogs'),
    path('contact', views.contact, name='contact')
    

]
