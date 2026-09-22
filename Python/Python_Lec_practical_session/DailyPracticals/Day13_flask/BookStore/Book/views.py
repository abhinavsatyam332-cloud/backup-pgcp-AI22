from flask import render_template

from . import app


books = [
    {
        'title': 'The Echo of Silent Winds',
        'author': 'Elena Rostova',
        'price': 45
    },
    {
        'title': 'Shadows in the Algorithm',
        'author': 'Marcus Vance',
        'price': 62
    },
    {
        'title': 'Beneath a Paper Moon',
        'author': 'Aria Sterling',
        'price': 38
    },
    {
        'title': 'Chronicles of the Iron Sky',
        'author': 'Devon Thorne',
        'price': 55
    },
    {
        'title': 'Whispers of the Forgotten Sea',
        'author': 'Lyra Belacqua',
        'price': 29
    },
    {
        'title': 'The Quantum Garden',
        'author': 'Julian Hayes',
        'price': 49
    },
    {
        'title': 'Midnight at St. Jude’s',
        'author': 'Clara O\'Connor',
        'price': 34
    },
    {
        'title': 'Architects of Tomorrow',
        'author': 'Siddharth Rao',
        'price': 70
    }
]

@app.route("/")
def home():
    return render_template('Home.html',books=books)

@app.route("/books")
def showData():
    return render_template('Books.html',books=books,title='Hello')

@app.route("/about")
def showData1():
    return render_template('About.html')

