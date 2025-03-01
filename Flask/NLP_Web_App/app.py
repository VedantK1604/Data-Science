
from flask import Flask,render_template,request,redirect, session
from db import Database
import api

app = Flask(__name__)
dbo = Database()

@app.route('/')
def index():
    # session['logged_in'] = 0
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/perform_registeration', methods=['post'])
def perform_registeration():
    name = request.form.get('user_name')
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    
    response =  dbo.insert(name,email,password)
    
    if response:
        return render_template('login.html', message = "Registration Successful. Kindly login to proceed.")
    else:
        return render_template('register.html',message = "Email Already Exists.")
    
@app.route('/perform_login', methods = ['post'])
def perform_login():
    email = request.form.get('user_email')
    password = request.form.get('user_password')
    
    response = dbo.search(email,password)
    
    if response:
        session['logged_in'] = 1
        return redirect('/profile')
    else:
        return render_template('login.html', login_message = 'incorrect email/password')

@app.route('/profile')
def profile():
    if session:
        return render_template('profile.html')
    else:
        return redirect('/')

@app.route('/ner')
def ner():
    if session:
        return render_template('ner.html')
    else:
        return redirect('/')

@app.route('/perform_ner',methods=['post'])
def perform_ner():
    if session:
        text = request.form.get('ner_text')
        response = api.ner(text)
        
        return render_template('ner.html',response = response)
    else:
        return redirect('/')

app.run(debug = True)