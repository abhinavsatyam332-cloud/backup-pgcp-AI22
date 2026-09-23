from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    return HttpResponse("<h1>Welcome to my book store</h1>")

def about(request):
    return HttpResponse("<h1>About Us</h1>")









books_data = [
    {"title": "The Echo of Silent Winds", "author": "Elena Rostova", "price": 45},
    {"title": "Shadows in the Algorithm", "author": "Marcus Vance", "price": 62},
    {"title": "Beneath a Paper Moon", "author": "Aria Sterling", "price": 38},
    {"title": "Chronicles of the Iron Sky", "author": "Devon Thorne", "price": 55},
    {"title": "Whispers of the Forgotten Sea", "author": "Lyra Belacqua", "price": 29},
]


def home(request):
    context = {'books':books_data}
    return render(request,'book/index.html',context)

def about(request):
    return render(request, 'book/about.html', {'title':'About us'})
