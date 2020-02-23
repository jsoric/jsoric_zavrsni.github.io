from datetime import datetime
from flask import Flask, redirect, url_for, render_template, request,abort,flash
from flask_sqlalchemy import SQLAlchemy
import webbrowser
import sqlite3  
from random import randrange
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


posts = [
    {
        'author': 'Josip Sorić',
        'title': 'Caribbean Cruises',
        'content': 'With an island for every taste, the Caribbean is the ultimate place for relaxation. You ll find white sands and turquoise water throughout the Caribbean Sea and Gulf of Mexico.',
        'date_posted': 'Siječanj 20, 2020'
    },
    {
        'author': 'John Doe',
        'title': 'Eastern Mediterranean',
        'content': 'if you re a fan of art and antiquities, a cruise to the Eastern Mediterranean is right up your alley. With itineraries that include the Adriatic/Dalmation Coast, Black Sea, Greek Isles and Holy Land, the region is a treasure trove for history lovers.',
        'date_posted': 'Siječanj 21, 2020'
    },
    {
        'author': 'John Doe',
        'title': 'Europe',
        'content': 'Your biggest difficulty planning a European cruise is narrowing down where you want to go. A Western Mediterranean itinerary usually includes stops in Barcelona and Monaco, as well as ports in Italy',
        'date_posted': 'Veljača 14, 2020'
    },
    {
        'author': 'John Doe',
        'title': 'Alaska',
        'content': 'The 49th State, the largest in the U.S., is perfect for cruisers, with numerous opportunities to appreciate its vast natural beauty.',
        'date_posted': 'Veljača 20, 2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


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
            print(email)
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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)