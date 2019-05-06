from flask import render_template, url_for, flash, redirect, request
from App import app, SQLdb, bcrypt
from App.dbs.SQLmodels import User, Review, Book
from App.frontend.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

posts = [
    {
        'author': 'Moisés Torres',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 28, 2019'
    },
    {
        'author': 'Moisés Torres',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 29, 2019'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/register", methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()

    # Conditional that checks if the registration is successful
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')  # The user's password is hashed
        user = User(username=form.username.data, email=form.email.data,
                    password=hashed_password)  # The user is created
        SQLdb.session.add(user)  # The user is added to the db
        SQLdb.session.commit()  # The changes of the db are commited
        flash('Account created successfully', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    # Conditional that checks if the login is successful
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')

    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template('account.html', title='Account')