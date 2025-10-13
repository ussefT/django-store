from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.shortcuts import get_object_or_404
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



def get_cart(req):
    cart=req.session.get('cart',[])
    if not cart or not isinstance(cart,list):
        cart=[]
    return cart

class AddToCartView(View):
    def get(self,request,id):

        # check product is exist or not
        obj=get_object_or_404(models.Product,id=id)
        # session :{ 'cart':[...] }
        cart=get_cart(request)
        cart.append(id)
        request.session['cart']=cart
        return HttpResponseRedirect(reverse('core:product_list'))

class RemoveToCartView(View):
    ...
class EmptyToCartView(View):
    ...
class ShowCartView(View):
    ...
class ChekoutCartView(View):
    ...

