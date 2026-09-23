from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Book
# Create your views here.

# books_data = [
#     {"title": "The Echo of Silent Winds", "author": "Elena Rostova", "price": 45},
#     {"title": "Shadows in the Algorithm", "author": "Marcus Vance", "price": 62},
#     {"title": "Beneath a Paper Moon", "author": "Aria Sterling", "price": 38},
#     {"title": "Chronicles of the Iron Sky", "author": "Devon Thorne", "price": 55},
#     {"title": "Whispers of the Forgotten Sea", "author": "Lyra Belacqua", "price": 29},
# ]


def home(request):
    # context = {'books':books_data}
    context = {'books':Book.objects.all()}

    return render(request,'book/index.html',context)

def about(request):
    return render(request, 'book/about.html', {'title':'About us'})

def book_details(request, book_id):
    mbook = get_object_or_404(Book, id=book_id)
    print(mbook)
    return render(request, 'book/book_details.html',{'title':'Book details', 'book':mbook})
