from flask import Flask,render_template,request,jsonify
import json
import time


app = Flask(__name__)

# Default
@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/Home.html')
def home():
    return render_template('Home.html')

@app.route('/staffs_login.html')
def staffs_login():
    return render_template('staffs_login.html')

@app.route('/staffs_signup.html')
def staffs_signup():
    return render_template('staffs_signup.html')

@app.route('/students_login.html')
def students_login():
    return render_template('students_login.html')

@app.route('/students_signup.html')
def students_signup():
    return render_template('students_signup.html')




if __name__ == '__main__':
    app.run(debug=True)
