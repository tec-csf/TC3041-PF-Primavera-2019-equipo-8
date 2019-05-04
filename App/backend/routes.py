from flask import render_template, url_for, flash, redirect
from App import app
from App.dbs.SQLmodels import User, Review
from App.frontend.forms import RegistrationForm, LoginForm

# Mongo pass: tx3lUZMAbWSbFAY0

posts = [
	{
		'author':'Moisés Torres',
		'title':'Blog Post 1',
		'content':'First post content',
		'date_posted':'April 28, 2019'
	},
	{
		'author':'Moisés Torres',
		'title':'Blog Post 2',
		'content':'Second post content',
		'date_posted':'April 29, 2019'
	}
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    #Flash message if the registration is successful
    if form.validate_on_submit():
    	flash(f'Account created for {form.username.data}!', 'success')
    	return redirect(url_for('home'))

    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
    	
    	#if form.email.data == '' and form.password.data == '':
    		#flash('You have benn logged in!', 'Success')
    	#else:
    		#flash('Login unsuccessful. Please check username and password', 'danger')

    	return redirect(url_for('home'))

    return render_template('login.html', title='Login', form=form)
