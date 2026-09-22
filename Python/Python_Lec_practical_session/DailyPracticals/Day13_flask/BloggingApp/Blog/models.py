from sqlalchemy import PrimaryKeyConstraint
from . import db

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    author = db.Column(db.String(120), nullable=False)
    content = db.Column(db.String(120), nullable=False)
    category = db.Column(db.String(120), nullable=False)
    date_posted = db.Column(db.String(120), nullable=False)


    def __repr__(self):
        return f'<Book {self.title}>'