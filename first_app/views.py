from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponse
# Create your views here.

def home_view(request):
    return render(request,'first_app/index.html',{'title':'Home'})
    
def privacy_view(request):
    return render(request,'first_app/privacy.html',{'title':'Privacy'})
    
def about_view(request):
    return render(request,'first_app/about.html',{'title':'About Us'})

def tutorial_view(request):
    return render(request,'first_app/tutorial.html',{'title':'Tutorial'})