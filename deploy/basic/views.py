from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html') # it render the output through home.html file   
