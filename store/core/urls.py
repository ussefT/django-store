from django.urls import path
from . import views

urlpatterns = [

    path('say',views.say,name='say'),
    
    path('',views.ListProduct.as_view(),name='list_product'),
]

# by default media is loaded for appServer
# django do not load media
# this if add url media to own url
from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)