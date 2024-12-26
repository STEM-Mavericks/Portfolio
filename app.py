from flask import Flask, render_template, flash, url_for, session, request, redirect
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app,secret_key = os.getenv('SECRET_KEY')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        flash('Please Log In First!','warning')
        return redirect(url_for('login'))
    return f"Welcome to your dashboard, {session['username']}!"

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username] == password:
            session['username'] = username
            flash('Login Successfull!', 'success')
            return redirect(url_for('login'))
        else:
            flash('Invalid Username or Password', 'danger')
        return render_template('login.html')

@app.route('/register', methods=['GET','POST'])
def register():
if __name__ == '__main__':
    app.run(debug=True)
