from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.

# function Based
# class Based


def say(request):
    return HttpResponse("Hi")

# when custome view, define every request on HTTP in class
class Say(View):
    # GET, POST, PUT, PATCH, DELETE, OPTIONS,...
    def get(self,request):
        return render(request,'say.html') 