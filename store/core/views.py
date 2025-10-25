from operator import invert

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import  JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.shortcuts import get_object_or_404
from . import models
from . import forms
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status
from rest_framework.permissions import AllowAny

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
    p=cart
    if not cart or not isinstance(cart,list):
        cart={}
    return cart


def  add_to_cart(cart,obj):
    """add to cart"""
    if obj.count>0 and obj.enabled:
        cart[str(obj.id)]=cart.get(str(obj.id),0)+1
    return cart

def remove_from_cart(cart,id):
    """remove from cart list"""
    if str(id) in cart:
        del cart[str(id)]

class AddToCartView(APIView):

    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self,request):
        """add to cart with get"""

        s=serializers.CartAddSerializer(data=request.data)
        if s.is_valid():
            try:
                # in class serializer
                id=s.validated_data['product_id']
                # check product is exist or not
                obj=models.Product.objects.get(id=id)

                # session :{ 'cart':{...} }
                cart=get_cart(request)
                add_to_cart(cart,obj)
                request.session['cart']=cart

                if request.headers.get('x-request-with')=='XMLHttpRequest':
                    return JsonResponse(cart)
                return HttpResponseRedirect(reverse('product_list'))
            except models.Product.DoesNotExist:
                return Response({'error':'Product not found'},status=status.HTTP_404_NOT_FOUND)
        return Response({'error':'bad request'},status=status.HTTP_400_BAD_REQUEST)
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
        return HttpResponseRedirect(reverse('core:product_list'))
class EmptyToCartView(View):
    def get(self,request):
        """empty cart with get"""
        request.session['cart']={}
        if request.is_ajax():
            return JsonResponse({})
        return HttpResponseRedirect(reverse('core/product_list'))

class GetCartAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self,request):
        cart=get_cart(request)
        s=serializers.CartShowSerializer(data=cart)
        return Response(s.data)
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
    def get(self,request):
        form=forms.InvoiceForm()
        return render(request,'core/checkout.html',{'form':form})

    def post(self,requset):
        form =forms.InvoiceForm(requset.POST)
        if form.is_valid():
            invoice=form.save(commit=False)
            invoice.user=requset.user
            cart=get_cart(requset)

            invoice.total=get_cart_total_price(cart)

            invoice.save()

            items=models.Product.objects.filter(id__in=cart.keys())

            item_objects=[]
            for item_id,item_count in cart.items():
                obj=items.get(id=item_id)
                invoice_item_obj=models.InvoiceItem()
                invoice_item_obj.invoice=invoice
                invoice_item_obj.product=obj
                invoice_item_obj.discount=obj.discount
                invoice_item_obj.price=obj.price
                invoice_item_obj.count=item_count
                invoice_item_obj.name=obj.name
                invoice_item_obj.total=invoice_item_obj.price*invoice_item_obj.count
                invoice_item_obj-=invoice_item_obj.total*invoice_item_obj.discount

                item_objects.append(invoice_item_obj)

            models.InvoiceItem.objects.bulk_create(item_objects)
            payment=models.Payment()
            payment.total=invoice.total - invoice.total * invoice.discount
            payment.total+=payment.total*invoice.vat
            payment.description='buy our site'
            payment.user_ip=get_user_ip(requset)

        #     Zarin pal
        #  redirect if ok payment

        return render(requset,'core/checkout.html',{'form':form})

class PayView(View):
    ...
class TestView(View):
    def get(self,req):
        obj=models.Product.objects.all().values("name","price")
        return JsonResponse(obj)

def get_user_ip(request):
    ip=request.META.get('HTTP_X_FORWARDED_FOR')
    if not ip:
        ip=request.META.get('REMOTE_ADDR')
    return ip


from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
class ProductListAPIView(APIView):

    # we can change permission this
    permission_classes = [
        IsAuthenticated,
    ]

    # authentication_classes = [
    #     TokenAuthentication,
    # ]

    def get(self,request,format=None):
        obj=models.Product.objects.all()
        s=serializers.ProductListSerializer(obj,many=True)
        return Response(s.data)

