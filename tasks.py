from flask import Flask, render_template, redirect, url_for, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'super secret key'

@app.route('/')
def home():

    if 'user' in session:
        return render_template("member.html")
    else:
        return render_template("guest.html")


app.run(debug=True)