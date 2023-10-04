from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
    
def contact(request):
    return render(request, 'contact.html')
    
def login(request):
    return render(request, 'accounts/login.html')
    
def logout(request):
    return render(request, 'accounts/logout.html')
    
def blog(request):
    return render(request, 'blog/base.html')
    
def blog1(request):
    return render(request, 'blog/1.html')
    
def blog2(request):
    return render(request, 'blog/2.html')
    
def blog3(request):
    return render(request, 'blog/3.html')
