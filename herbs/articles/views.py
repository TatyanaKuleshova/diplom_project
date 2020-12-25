from django.shortcuts import render

def index(request):
    return render(request, 'articles/index.html')

def properties(request):
    return render(request, 'articles/properties.html')

def catalog(request):
    return render(request, 'articles/catalog.html')

def literatura(request):
    return render(request, 'articles/literatura.html')

def article(request):
    return render(request, 'articles/article.html')

def registration(request):
    return render(request, 'articles/registration.html')