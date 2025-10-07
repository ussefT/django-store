from django.shortcuts import render
from django import views
# Create your views here.
from . import form
#class base
#  views.View
#  Generic [TemplateView, ListView, DetailView .....] write by default django
class SignUpView(views.View):
    def get(self,request):
        """show sign up form"""
        form_=form.SignupForm()
        return render(request
                      ,'account/signUp.html'
                      ,{'form':form_})
    def post(self,request):
        """create new user from form """
        pass