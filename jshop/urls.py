from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product-details", views.product_details, name="product-details"),
    path("login", views.login, name="login"),
    
]