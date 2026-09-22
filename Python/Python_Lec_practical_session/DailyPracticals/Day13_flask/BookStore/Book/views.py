
from flask import render_template, redirect, url_for

from . import app
from .models import Book
from .forms import RegistrationForm

books=[]

@app.route("/")
def index():
    books = Book.query.all()
    return render_template('home.html',books=books)


@app.route("/home")
def home():
    books = Book.query.all()
    return render_template('Home.html',books=books)


@app.route("/about")
def about():
    return render_template('About.html')


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    else:
        print(form.errors)
    return render_template('register.html',title='Register',form=form)


@app.route('/book/<int:book_id>')
def book_details(book_id):
    book = Book.query.get_or_404(book_id)
    return render_template('book_details.html',book = book)
