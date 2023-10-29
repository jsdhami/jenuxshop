from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product-details", views.product_details, name="product-details"),
    path("login", views.loginPage, name="login"),
    path("signup", views.signupPage, name="signup"),
    path("404", views.foferror, name="404"),
    path("blog-single", views.blog_single, name="blog-single"),
    path("blog", views.blog, name="blog"),
    path("cart", views.cart, name="cart"),
    path("checkout", views.checkout, name="checkout"),
    path("shop", views.shop, name="shop"),
    path("contact-us", views.contact_us, name="contact-us"),
    path("logout", views.logoutPage, name="logout"),
    path("profile", views.profile, name="name"),
    path("test", views.test, name="test")
    
]