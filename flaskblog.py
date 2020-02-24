from datetime import datetime
from flask import Flask, redirect, url_for, render_template, request,abort,flash
from flask_sqlalchemy import SQLAlchemy
import webbrowser
import sqlite3  
from random import randrange
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/gallery")
def gallery():
    return render_template('gallery.html', title='Gallery')

@app.route("/subscribe")
def subscribe():
   return render_template("subscribe.html")

@app.route("/save",methods = ["POST","GET"])
def save():
    msg = "msg"  
    if request.method == "POST":  
        try:  
            name = request.form["name"]  
            email = request.form["email"] 
            with sqlite3.connect("subscribe.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Subscribers (name, email) values (?,?)",(name,email))  
                con.commit()  
                msg = "User successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the user to the list"  
        finally:  
             return render_template("about.html")  
             con.close()   

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        try:
            ime=form.name.data
            prezime=form.surname.data
            email=form.email.data
            spol=form.gender.data
            with sqlite3.connect("subscribe.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Register (name, surname, email, spol) values (?,?,?,?)",(ime,prezime,email,spol))  
                con.commit()  
                msg = "User successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the user to the list"  
        finally:  
             con.close()   
        flash(f'Sretan put {form.name.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
if __name__ == '__main__':
    app.run(debug=True)