from flask import Flask, render_template, flash, redirect, url_for
from forms_and_requests import LoginForm, RegistrationForm

app = Flask(__name__)

# a secret key to protect from cookies and fake requests
# an easy way to generate a big random number is:
#   >>> import secrets
#   >>> secrets.token_hex(16)
#   >>> exit()
app.config['SECRET_KEY'] = '942e6da3614c14c315b7fa767a49d510'

posts = [
    {"author" : "Houss", "title" : "blog 1", "content" : "introduction to python", "added_time" : "12.4.2020"},
    {"author" : "Ouss", "title": "blog 2", "content" : "flask and html", "added_time" : "12.4.2020"}
]

@app.route('/home')
def homepage():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='Tutorials')

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    # flash : is a module in flask to send a signal (alert or feedback) to make sure the user logged in successfully

    if form.validate_on_submit(): # this tell us if our form validated after submited
        flash(f'Account created successfully for { form.username.data }!', 'success')
        # the second arg is called a category : 'success' this is for bootstraps to know what class of alert
        # after login redirect function sends the user the a specific page ( in this case homepage)
        return redirect(url_for('homepage'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template('login.html', title='login', form=form)


if __name__ == "__main__":
    app.run(debug=True)