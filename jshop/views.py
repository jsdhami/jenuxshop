from django.shortcuts import render, redirect
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test


def user_is_logged_out(user):
    return not user.is_authenticated



def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html')


def logoutPage(request):
    logout(request)
    now_page = request.GET.get('next')
    if now_page:
        return redirect(now_page)
    else:
        return redirect('index')
    

@user_passes_test(user_is_logged_out, login_url='index')
def loginPage(request): 
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            next_url = request.GET.get('next')
            if user is not None:
                login(request, user)
                if next_url:
                    return redirect(next_url)
                                   
            else:
                return HttpResponse("don't matched password and username")
        return render(request, 'login.html')
    
@user_passes_test(user_is_logged_out, login_url='index')
def signupPage(request):
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

@login_required(login_url='login')
def checkout(request):
    
    return render(request, 'checkout.html')

def shop(request):
    
    return render(request, 'shop.html')

def contact_us(request):
    
    return render(request, 'contact-us.html')



  
    
   