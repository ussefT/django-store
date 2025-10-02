from django.urls import path
from . import views

urlpatterns = [

    path('say',views.say,name='say'),
    path('say2',views.Say.as_view,name='say2'),
]