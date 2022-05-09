from config import connection
from flask import Flask, render_template, request, redirect, url_for

application = Flask(__name__)

@application.route('/')
def home():
    return render_template('home.html')

@application.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']

        query = '''INSERT INTO users VALUES (%s, %s);'''
        #Execute query
        connection.execute(query, [first_name, last_name])

        return redirect(url_for('home'))
    else:
        return render_template('register.html')

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.run(debug = True)
