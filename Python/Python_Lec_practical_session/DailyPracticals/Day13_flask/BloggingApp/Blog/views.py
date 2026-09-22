from flask import render_template,redirect,url_for

from  . import app

blogs = [
    {
        'id': 1,
        'title': 'Getting Started with Flask and Python',
        'author': 'Alex Mercer',
        'content': 'Flask is a lightweight WSGI web application framework in Python. It is designed to make getting started quick and easy...',
        'category': 'Web Development',
        'date_posted': '2026-01-15'
    },
    {
        'id': 2,
        'title': 'Understanding Object-Relational Mapping with SQLAlchemy',
        'author': 'Sophia Chen',
        'content': 'SQLAlchemy provides a full suite of well-known enterprise-level persistence patterns, designed for efficient and high-performing database access...',
        'category': 'Database',
        'date_posted': '2026-02-02'
    },
    {
        'id': 3,
        'title': 'Mastering Jinja2 Template Inheritance',
        'author': 'David Miller',
        'content': 'Template inheritance allows you to build a base layout that contains all the common elements of your site and defines blocks that child templates can override...',
        'category': 'Frontend',
        'date_posted': '2026-03-10'
    },
    {
        'id': 4,
        'title': 'Building Secure Authentication Forms with WTForms',
        'author': 'Elena Rostova',
        'content': 'Validating user input and defending against CSRF attacks is crucial for any web app. WTForms makes rendering and validating forms simple...',
        'category': 'Security',
        'date_posted': '2026-04-18'
    },
    {
        'id': 5,
        'title': 'Deploying Python Applications to the Cloud',
        'author': 'Marcus Vance',
        'content': 'Once your local Flask development server is running smoothly, learn how to containerize and deploy your application to cloud platforms...',
        'category': 'DevOps',
        'date_posted': '2026-05-22'
    }
]

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/getblogs")
def getblogs():
    return render_template('blogss.html',blogs = blogs)

@app.route('/newblog')
def newblog():
    return render_template('newblog.html')
