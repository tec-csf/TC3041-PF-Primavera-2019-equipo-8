from flask import render_template, url_for, flash, redirect, request, session
from App import app, SQLdb, bcrypt, Session
from App.dbs.SQLmodels import User, Reviews, Book
from App.frontend.forms import RegistrationForm, LoginForm, UpdateAccountForm, ReviewForm
import secrets
import os

# Route for the page of each book
@app.route('/<bookid>', methods=['GET', 'POST'])
def image_page(bookid):

    if not 'username' in session:
        flash('You have to log in to access the books', 'danger')
        return redirect(url_for('home'))

    book = Book.query.filter_by(id=bookid).first()

    username = session['username']
    user = User.query.filter_by(username=username).first()

    reviews = Reviews.query.filter_by(book_id=bookid)

    for review in reviews:
        review.username = User.query.filter_by(id=review.user_id).first().username

    form = ReviewForm()

    if form.validate_on_submit():
        review = Reviews(content=form.content.data,
                         user_id=user.id, book_id=book.id)
        SQLdb.session.add(review)
        SQLdb.session.commit()
        flash('Review submitted', 'success')
        return redirect(url_for('home'))

    return render_template('book.html', book=book, reviews=book.reviews, form=form)


# Route for the home page
@app.route("/")
@app.route("/home")
def home():
    # Get all the books
    books = Book.query.filter_by()
    return render_template('home.html', books=books)


# Route for the register page
@app.route("/register", methods=['GET', 'POST'])
def register():

    if 'username' in session:
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
        flash('Account created successfully. You can log in now.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


# Route for the login page
@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if 'username' in session:
        return redirect(url_for('home'))

    # Conditional that checks if the login is successful
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['username'] = user.username
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check email and password', 'danger')

    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        app.root_path, 'frontend\\static\\profile_pics', picture_fn)
    form_picture.save(picture_path)

    return picture_fn


@app.route("/account", methods=['GET', 'POST'])
def account():

    if not 'username' in session:
        return redirect(url_for('home'))

    username = session['username']
    user = User.query.filter_by(username=username).first()

    form = UpdateAccountForm()

    if form.validate_on_submit():

        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            user.image_file = picture_file

        user.username = form.username.data
        user.email = form.email.data
        SQLdb.session.commit()

        session.pop('username', None)
        session['username'] = user.username

        flash('Your account has been updated', 'success')
        return redirect(url_for('account'))

    elif request.method == 'GET':
        form.email.data = user.email    
        form.username.data = user.username
        

    image_file = url_for(
        'static', filename='profile_pics/' + user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form, user=user)
