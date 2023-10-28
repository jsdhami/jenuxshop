from django.urls import path
from . import views

urlpatterns = [
    # path("", views.home, name="home"),
    path("hello/", views.catagory, name="caatagory")   
]