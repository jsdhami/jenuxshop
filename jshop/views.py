from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")

    return render(request, 'index.html')


def login(request):
    
    return render(request, 'login.html')

def signup(request):
    if request.method== 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        my_user = User.objects.create_user(username, email, password)
        my_user.save()
        return redirect('login')
    
    
    return render(request, 'signup.html')


def product_details(request):
    
    return render(request, 'product-details.html')

def foferror(request):
    
    return render(request, '404.html')

def blog(request):
    
    return render(request, 'blog.html')


def blog_single(request):
    
    return render(request, 'blog-single.html')

def cart(request):
    
    return render(request, 'cart.html')


def checkout(request):
    
    return render(request, 'checkout.html')

def shop(request):
    
    return render(request, 'shop.html')

def contact_us(request):
    
    return render(request, 'contact-us.html')