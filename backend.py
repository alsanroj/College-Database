from flask import Flask,render_template,request,jsonify
import json
import time
import mysql.connector

# MySQL Credentials
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="01062006",
        database="college_db"
    )
    cursor = conn.cursor()
except mysql.connector.Error as err:
    print(f"Error: {err}")
    conn = None
    cursor = None

app = Flask(__name__)

# Default
@app.route('/')
def index():
    return render_template('students_login.html')

@app.route('/staffs_login.html')
def staffs_login():
    return render_template('staffs_login.html')

@app.route('/staffs_signup.html')
def staffs_signup():
    return render_template('staffs_signup.html')

@app.route('/students_login.html')
def students_login():
    return render_template('students_login.html')





if __name__ == '__main__':
    app.run(debug=True)
