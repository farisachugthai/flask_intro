"""Practice module for an intro to flask."""
from flask import Flask, redirect, render_template, request, url_for

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url


@app.route('/')
def home():
    """Return a basic string."""
    return "Hello, World!"  # return a string


@app.route('/welcome')
def welcome():
    """Let's return HTML."""
    return render_template('welcome.html')  # render a template

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handle simple logic."""
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
