from flask import render_template

from . import app
from .models import Book

books=[]

@app.route("/")
def index():
    books = Book.query.all()
    return render_template('index.html',books=books)


@app.route("/home")
def home():
    books = Book.query.all()
    return render_template('Home.html',books=books)

@app.route("/books")
def showData():
    return render_template('Books.html',books=books,title='Hello')

@app.route("/about")
def about():
    return render_template('About.html')

@app.route("/register")
def register():
    return render_template('About.html')

@app.route('/book/<int:book_id>')
def book_details(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_details.html',book = book)
