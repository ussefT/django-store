from django.urls import path
from . import views
urlpatterns = [
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('activate/<user>/<hash>', views.ActivateView.as_view(), name='activate'),

]