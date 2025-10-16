from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import  JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.shortcuts import get_object_or_404
from . import models
# Create your views here.

# function Based
# class Based

# when custome view, define every request on HTTP in class
class ListProduct(View):
    # GET, POST, PUT, PATCH, DELETE, OPTIONS,...
    def get(self,request):
        # get objects from model
        object=models.Product.objects.all()
        return render(request,'core/ListProduct.html',{'products':object})


def get_cart_total_price(cart):
    """get the total price of the cart"""
    total=0
    objects=models.Product.objects.filter(id__in=list(cart.keys()))
    for id,count in cart.items():
        obj=objects.get(id=id)
        total+=(obj.price-obj.price * obj.discount) * count
    return total

def get_cart(req):
    """get cart from request"""
    cart=req.session.get('cart',{})
    if not cart or not isinstance(cart,list):
        cart={}
    return cart


def  add_to_cart(cart,obj):
    """add to cart"""
    if obj.count>0 and obj.enabled:
        cart[obj.id]=cart.get(str(obj.id),0)+1
    return cart

def remove_from_cart(cart,id):
    """remove from cart list"""
    if str(id) in cart:
        del cart[str(id)]

class AddToCartView(View):
    def get(self,request,id:int):
        """add to cart with get"""
        # check product is exist or not
        obj=get_object_or_404(models.Product,id=id)
        # session :{ 'cart':{...} }
        cart=get_cart(request)
        add_to_cart(cart,obj)
        request.session['cart']=cart
        if request.headers.get('x-request-with')=='XMLHttpRequest':
            return JsonResponse(cart)
        return HttpResponseRedirect(reverse('core/product_list'))

class RemoveToCartView(View):
    def get(self,request,id):
        """remove from cart list with get"""
        cart=get_cart(request)
        remove_from_cart(cart,id)
        request.session['cart']=cart
        if request.request.headers.get('x-request-with')=='XMLHttpRequest':
            return JsonResponse({
                'total':get_cart_total_price(cart),
                'cart':cart,
            })
        return HttpResponseRedirect(reverse('core/product_list'))
class EmptyToCartView(View):
    def get(self,request):
        """empty cart with get"""
        request.session['cart']={}
        if request.is_ajax():
            return JsonResponse({})
        return HttpResponseRedirect(reverse('core/product_list'))
class ShowCartView(View):
    def get(self,request):
        cart=get_cart(request)
        objects=(models.
                 Product.objects.filter(id__in=list(cart.keys())))
        cart_objects={}
        for id,count in cart.items():
            obj=objects.get(id=id)
            cart_objects[id] = {
                'obj':obj,
                'price':(obj.price-obj.price * obj.discount) * count,
                'count':count,
            }
        return render(request,'core/cart.html',
               {'cart':cart_objects
                   ,'total':get_cart_total_price(cart)})
class ChekoutCartView(View):
    ...

class TestView(View):
    def get(self,req):

        obj=models.Product.objects.all().values("name","price")
        return JsonResponse(obj)