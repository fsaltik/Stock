from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html', {})

def about(requst):
    return  render(requst,'about.html',{})