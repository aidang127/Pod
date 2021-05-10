import os

from dominate.tags import var
from flask_wtf.file import FileField
from pkg_resources import require
from sqlalchemy import sql

from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from os import path
import sqlite3 as sql
from datetime import datetime




class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


ROOT = os.path.dirname(os.path.relpath(("_file_")))

def create_post(name,content):
    con=sql.connect(path.join(ROOT,'database.db'))
    cur = con.cursor()
    cur.execute('insert into posts (name, content) values(?,?)', (name, content))
    con.commit()
    con.close()

def get_posts():
    con = sql.connect(path.join(ROOT,'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    return posts







