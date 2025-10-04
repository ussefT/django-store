from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . import models
# Create your views here.

# function Based
# class Based


def say(request):
    return HttpResponse("Hi")

# when custome view, define every request on HTTP in class
class ListProduct(View):
    # GET, POST, PUT, PATCH, DELETE, OPTIONS,...
    def get(self,request):
        # get objects from model
        object=models.Product.objects.all()
        return render(request,'core/ListProduct.html',{'product':object}) 