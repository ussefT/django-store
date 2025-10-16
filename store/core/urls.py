from django.urls import path
from . import views

urlpatterns = [
    path('',views.ListProduct.as_view(),name='list_product'),
    path('cart/add/<int:id>', views.AddToCartView.as_view(), name='cart_add'),
    path('cart/remove/<int:id>', views.RemoveToCartView.as_view(), name='cart_remove'),
    path('cart/empty', views.EmptyToCartView.as_view(), name='cart_empty'),
    path('cart', views.ShowCartView.as_view(), name='cart_show'),
    path('checkout', views.ChekoutCartView.as_view(), name='checkout'),


    path('test',views.TestView.as_view(),name='test'),
]

# by default media is loaded for appServer
# django do not load media
# this if add url media to own url
from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)