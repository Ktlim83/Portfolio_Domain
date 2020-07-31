from django.shortcuts import render, redirect, HttpResponse


def dashboard(request):
    
    return render(request, 'index.html', {})


def blog(request):
    
    return render(request, 'blog.html', {})