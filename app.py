from flask import Flask, render_template, redirect, url_for, request
from random import randint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TextField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import os
import json
import sqlite3

from flask import Flask, redirect, request, url_for
from flask_login import UserMixin, current_user, login_user, login_required, logout_user, LoginManager
import requests

from db import init_db_command
from user import User
from authlib.integrations.flask_client import OAuth

from config import Config
import datetime
import sqlite3 as sql

app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager()
login_manager.init_app(app)

basedir = os.path.abspath(os.path.dirname(__file__))

#YOUR APP INITIALIZATION GOES HERE

oauth = OAuth(app)
oauth.register(
    name="google",
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Breakfast, Lunch, Tea, User
from forms import LoginForm, BreakfastForm, LunchForm, TeaForm

#flask_login.login_required()
login_manager.login_view = "/"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route("/authorize")
def authorize():
    #Accessing specific parts of user's email account
    token = oauth.google.authorize_access_token()
    oauth_user = oauth.google.parse_id_token(token)

    
    #verifying if it is school user
    if "tes.tp.edu.tw" in oauth_user["email"]:
        user = User.query.filter_by(email=oauth_user["email"]).first()
        if not user:
            user = User(
                name=oauth_user["name"],
                email=oauth_user["email"],
                )

            db.session.add(user)
            db.session.commit()
        login_user(user)
        #verifying if it is an admin account
        if "student.council@stu.tes.tp.edu.tw" in oauth_user["email"]:
            role = "Admin"
            return redirect("admin")
        else:
            return redirect("welcome")

    render_template("")


@app.route("/oauth_login/<provider_name>/", methods=["GET", "POST"])
def oauth_login(provider_name):
    """Login access for oauth."""
    redirect_uri = url_for("authorize", _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

from flask import session

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("welcome"))
    return redirect(url_for("home"))

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))

from flask import g

database = "app.db"
@app.route('/viewbreakfast')
@login_required
def viewbreakfast():
    #verifying if user is an admin account
    if current_user.email != "student.council@stu.tes.tp.edu.tw":
        return render_template("welcome.html")

    #connecting app.py to app.db to obtain database information
    conn = sqlite3.connect("app.db")
    with sql.connect("app.db") as con:
            cur = con.cursor()
    con.row_factory = sql.Row
       
    cur = con.cursor()
    cur.execute("select * from breakfast")

    rows = cur.fetchall(); 
    conn.close()
    return render_template("viewbreakfast.html", rows = rows)


@app.route('/viewlunch')
@login_required
def viewlunch():
    if current_user.email != "student.council@stu.tes.tp.edu.tw":
        return render_template("welcome.html")

    conn = sqlite3.connect("app.db")
    with sql.connect("app.db") as con:
            cur = con.cursor()
    con.row_factory = sql.Row
       
    cur = con.cursor()
    cur.execute("select * from lunch")

    rows = cur.fetchall(); 
    conn.close()
    return render_template("viewlunch.html", rows = rows)

@app.route('/viewtea')
@login_required
def viewtea():
    if current_user.email != "student.council@stu.tes.tp.edu.tw":
        return render_template("welcome.html")

    conn = sqlite3.connect("app.db")
    with sql.connect("app.db") as con:
            cur = con.cursor()
    con.row_factory = sql.Row
       
    cur = con.cursor()
    cur.execute("select * from tea")

    rows = cur.fetchall(); 
    conn.close()
    return render_template("viewtea.html", rows = rows)


@app.route('/')
def home():
   return render_template("home.html")

@app.route('/admin')
@login_required
def admin():
    #authenticating if it's admin account -- if admin account go to admin page
    if current_user.email != "student.council@stu.tes.tp.edu.tw":
        return render_template("welcome.html")
    else:
        return render_template("admin.html")

@app.route('/welcome')
@login_required
def welcome():
    return render_template("welcome.html")

@app.route('/sales')
@login_required
def sales():
    return render_template("sales.html")

@app.route('/myaccount')
def myaccount():
    return render_template("myaccount.html", name=current_user.name, email=current_user.email)

@app.route('/confirmorder')
@login_required
def confirmorder():
    return render_template("confirmorder.html")

def clear_data(session):
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        session.execute(table.delete())
    session.commit()

@app.route('/orderbreakfast', methods=('GET','POST'))
@login_required
def orderbreakfast():
    #Calling in form used to be BreakfastForm, as created in forms.py
    form = BreakfastForm()
    if request.method == 'POST':
        breakfast = Breakfast()
        
        #Data added to each field in database
        breakfast.name = current_user.name
        breakfast.email = current_user.email
        breakfast.date = datetime.datetime.now()
        breakfast.burger = request.form['burger']
        breakfast.cheese = request.form['cheese']
        breakfast.bacon = request.form['bacon']
        breakfast.hashbrown = request.form['hashbrown']
        db.session.add(breakfast)
        db.session.commit()
        return render_template("ordercomplete.html")
    return render_template("orderbreakfast.html", form=form)

@app.route('/ordertea', methods=('GET','POST'))
@login_required
def ordertea():
    form = TeaForm()
    if request.method == 'POST':
        tea = Tea()
        tea.name = current_user.name
        tea.email = current_user.email
        tea.date = datetime.datetime.now()
        tea.passionfruit = request.form['passionfruit']
        tea.milktea = request.form['milktea']
        db.session.add(tea)
        db.session.commit()
        return render_template("ordercomplete.html")
    return render_template("ordertea.html", form=form)


@app.route('/orderlunch', methods=('GET','POST'))
@login_required
def orderlunch():
    form = LunchForm()
    if request.method == 'POST':
        lunch = Lunch()
        lunch.name = current_user.name
        lunch.date = datetime.datetime.now()
        lunch.email = current_user.email
        lunch.fries = request.form['fries']
        db.session.add(lunch)
        db.session.commit()
        return render_template("ordercomplete.html")
    return render_template("orderlunch.html", form=form)

if __name__ == '__main__':
    app.run()
