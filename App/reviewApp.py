from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

#Secret key
app.config['SECRET_KEY'] = '83a06f37055cbb6f8eb86a4a2608748c'

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

if __name__ == '__main__':
	app.run(debug=True)