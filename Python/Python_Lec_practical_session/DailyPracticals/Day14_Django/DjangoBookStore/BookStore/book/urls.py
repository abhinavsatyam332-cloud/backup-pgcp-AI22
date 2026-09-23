from django.urls import path
from  . import views

urlpatterns = [
    path('',views.home, name='book-home'),
    path('about/',views.about, name='book-about'),
    path('book_details/<int:book_id>',views.book_details,name = 'book-details')
]
