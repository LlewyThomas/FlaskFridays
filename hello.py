from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Create a Flask Instance
app = Flask(__name__)
# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# Create Secret Key
app.config['SECRET_KEY'] = "my supper secret key that no one is suppose to know" # CSRF Token for WTForms
# Initialize the Database
db = SQLAlchemy(app)

# Create Model for Database
class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200), nullable= False)
    email = db.Column(db.String(120), nullable= False, unique=True)
    date_added = db.Column(db.DateTime,default=datetime.utcnow)

    # Create a String
    def __repr__(self):
        return '<Name %r>' % self.name
 
 # Create a Form Class
class UserForm(FlaskForm):
    name = StringField("Name",validators=[DataRequired()])
    email = StringField("Email",validators=[DataRequired()])
    submit = SubmitField("Submit")


# Create a Form Class
class NamerForm(FlaskForm):
    name = StringField("What's Your Name",validators=[DataRequired()])
    submit = SubmitField("Submit")



# Create a route decorator
@app.route('/')

def index():

    first_name = "Llewy"
    stuff = "This is <strong> Bold. </strong>"
    favorite_pizza = ["Pepperoni","Magaretta","Vegatarian",41]

    return render_template('index.html',
        first_name=first_name,
        stuff=stuff,
        favorite_pizza=favorite_pizza)

# Create a route decorator
@app.route('/user/add', methods=['GET','POST'])

def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first() # make sure the email doesnt already exist in db
        if user is None: # if user is None then email doesn't exist in db, so go ahead and add user to db
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
            db.session.commit()
        name = form.name.data
        form.name.data = '' # clear the form
        form.email.data = ''
        flash("User Added Successfully!")
    
    our_users = Users.query.order_by(Users.date_added)
    return render_template("add_user.html",
        form=form,
        name=name,
        our_users =our_users)

@app.route('/user/<name>')

def user(name):
    return render_template('user.html',user_name=name)

# Create Custom Error Pages

# Invalid URL 
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

# Create Name Page
@app.route('/name', methods=['GET','POST'])
def name():
    name = None
    form = NamerForm()
    # Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfully!")
    return render_template('name.html',
        name = name,
        form = form)