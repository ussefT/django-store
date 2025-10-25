from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

urlpatterns = [
    path('',views.ListProduct.as_view(),name='product_list'),
    path('cart/add/<int:id>', views.AddToCartView.as_view(), name='cart_add'),
    path('cart/remove/<int:id>', views.RemoveToCartView.as_view(), name='cart_remove'),
    path('cart/empty', views.EmptyToCartView.as_view(), name='cart_empty'),
    path('cart', views.ShowCartView.as_view(), name='cart_show'),
    path('checkout', views.ChekoutCartView.as_view(), name='checkout'),
    path('pay', views.PayView.as_view(), name='pay'),


    path('api/product',views.ProductListAPIView.as_view(),name='api_product'),
    path('api/cart',views.GetCartAPIView.as_view(),name='api_cart'),

    #  for get token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # for refresh token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

# by default media is loaded for appServer
# django do not load media
# this if add url media to own url
from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)