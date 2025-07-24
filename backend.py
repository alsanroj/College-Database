from logging import error
from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import pymysql
import json
import os
import time
import re


app = Flask(__name__)
app.secret_key = 'b2e3c7e8f4a1d9c6e5b8f7a2c3d4e6f1a9b0c8d7e3f2a6b5c4d1e8f7a3b6c9d0' # Paste a strong and random secret key of your own desire.

#MySQL Database Details
database = pymysql.connect(
    host="localhost",
    user="root",
    password="01062006",
    database="college_db"
)

cursor = database.cursor()

# Default (Home page)
@app.route('/')
def index():
    return render_template('Home.html')




# Home Page
@app.route('/Home.html')
def home():
    return render_template('Home.html')




# Staffs Login
@app.route('/staffs_login.html', methods=['GET', 'POST'])
def staffs_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            error = "Username and password are required"
            return render_template('staffs_login.html', error=error)
        cursor.execute("SELECT * FROM staffs WHERE BINARY staff_rollno=%s AND BINARY staff_password=%s", (username, password))
        staff = cursor.fetchone()
        print(staff)
        if staff:
            return render_template('staff_dashboard.html', staff=staff)
        else:
            error = "Invalid username or password"
            return render_template('staffs_login.html', error=error)
    return render_template('staffs_login.html')




# Staffs Signup
@app.route('/staffs_signup.html', methods=['GET', 'POST'])
def staffs_signup():
    if request.method == 'POST':
        staff_name = request.form.get('staff_Name')
        staff_rollno = request.form.get('staff_Rollno')
        staff_email = request.form.get('staff_email')
        staff_phonenumber = request.form.get('staff_phNumber')
        staff_password = request.form.get('staff_password')
        staff_repassword = request.form.get('staff_rePassword')

        #Checks for valid role number
        if not staff_rollno or not re.match(r'^T[A-Z]{2}\d{2}$', staff_rollno):
            error = "Roll number must be in this format: T, Department Name, Unique Number of the Staff \n (e.g., TEE40)"
            return render_template('staffs_signup.html', error=error)

        #Checks wheather the phone number is 10 digit ot not
        if not staff_phonenumber or not re.match(r'^\d{10}$', staff_phonenumber):
            error = "The Phone Number must contain 10 digits"
            return render_template('staffs_signup.html', error=error)

        #Checks for the password and re-password match
        if not staff_password or len(staff_password) < 16:
            error = "Password must contain at least 16 characters"
            return render_template('staffs_signup.html', error=error)

        if staff_password != staff_repassword:
            error = "Passwords do not match"
            return render_template('staffs_signup.html', error=error)

        #Checks for Roll No duplicate
        cursor.execute("SELECT * FROM staffs WHERE staff_rollno=%s", (staff_rollno,))
        if cursor.fetchone():
            error = "User already registered"
            return render_template('staffs_signup.html', error=error)

        #Inserts the new user (STAFF) into the database
        cursor.execute(
            "INSERT INTO staffs (staff_name, staff_rollno, staff_email, staff_phonenumber, staff_password) VALUES (%s, %s, %s, %s, %s)",
            (staff_name, staff_rollno, staff_email, staff_phonenumber, staff_password)
        )
        database.commit()
        cursor.execute("SELECT * FROM staffs WHERE staff_rollno=%s", (staff_rollno,))
        staff = cursor.fetchone()
        print(staff)
        if staff:
            return render_template('staff_dashboard.html', staff=staff)
        else:
            error = "An error occurred during registration"
            return render_template('staffs_login.html', error=error)
    return render_template('staffs_signup.html')




#Students Login
@app.route('/students_login.html', methods=['GET', 'POST'])
def students_login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            error = "Username and password are required"
            return render_template('students_login.html', error=error)
        cursor.execute("SELECT * FROM students WHERE BINARY student_rollno=%s AND BINARY student_password=%s", (username, password))
        student = cursor.fetchone()
        print(student)
        if student:
            session['student_logged_in'] = True  # Set session variable
            session['student_roll_no'] = username  # Optionally store roll_no
            return redirect(url_for('students_dashboard'))
        else:
            error = "Invalid username or password"
            return render_template('students_login.html', error=error)
    return render_template('students_login.html')




# Students Signup
@app.route('/students_signup.html', methods=['GET', 'POST'])
def students_signup():
    if request.method == 'POST':
        student_name = request.form.get('student_Name')
        student_rollno = request.form.get('student_Rollno')
        student_email = request.form.get('student_email')
        student_phonenumber = request.form.get('student_phNumber')
        student_password = request.form.get('student_password')
        student_repassword = request.form.get('student_rePassword')

        #Checks for valid role number
        if not student_rollno or not re.match(r'^\d{2}[A-Z]{2}\d{3}$', student_rollno):
            error = "Roll number must be in this format: Year of Admission , Department Name, Unique Number of the Student \n (e.g., 23EE271)"
            return render_template('students_signup.html', error=error)

        #Checks wheather the phone number is 10 digit ot not
        if not student_phonenumber or not re.match(r'^\d{10}$', student_phonenumber):
            error = "The Phone Number must contain 10 digits"
            return render_template('students_signup.html', error=error)

        #Checks for the password and re-password match
        if not student_password or len(student_password) < 16:
            error = "Password must contain at least 16 characters"
            return render_template('students_signup.html', error=error)
        if student_password != student_repassword:
            error = "Passwords do not match"
            return render_template('students_signup.html', error=error)

        #Checks for email duplicate
        cursor.execute("SELECT * FROM students WHERE student_email=%s", (student_email,))
        if cursor.fetchone():
            error = "Email already registered"
            return render_template('students_signup.html', error=error)

        #Inserts the new user (STUDENT) into the database
        cursor.execute(
            "INSERT INTO students (student_rollno, student_name, student_email, student_phonenumber, student_password) VALUES (%s, %s, %s, %s, %s)",
            (student_rollno, student_name, student_email, student_phonenumber, student_password)
        )
        database.commit()
        cursor.execute("SELECT * FROM students WHERE student_email=%s", (student_email,))
        student = cursor.fetchone()
        print(student)
        if student:
            session['student_logged_in'] = True
            session['student_roll_no'] = student_rollno
            return redirect(url_for('students_dashboard'))
        else:
            error = "An error occurred during registration"
            return render_template('students_login.html', error=error)
    return render_template('students_signup.html')




# Students Dashboard
@app.route('/students_dashboard.html', methods=['GET', 'POST'])
def students_dashboard():
    if not session.get('student_logged_in'):
        return redirect(url_for('students_login'))
    if request.method == 'POST':
        student_register_number = request.form.get('register_number')
        student_roll_no = request.form.get('roll_no')
        student_name = request.form.get('student_name')
        student_gender = request.form.get('student_gender')
        student_dob = request.form.get('student_dob')
        student_father_name = request.form.get('father_name')
        student_fathers_phone_no = request.form.get('fathers_phone_no')
        student_mother_name = request.form.get('mother_name')
        student_mothers_phone_no = request.form.get('mothers_phone_no')
        student_email = request.form.get('email')
        student_phone_no = request.form.get('students_phone_no')
        student_aadhar_number = request.form.get('aadhar_number')
        student_nationality = request.form.get('nationality')
        student_religion = request.form.get('religion')
        student_community = request.form.get('community')
        student_caste = request.form.get('caste')
        
        cursor.execute(
            "INSERT INTO student_personal_details (register_number, roll_no, name, gender, date_of_birth, father_name, father_mobile, mother_name, mother_mobile, mail, student_mobile, aadhar_number, nationality, religion, community, caste) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            (student_register_number, student_roll_no, student_name, student_gender, student_dob, student_father_name, student_fathers_phone_no, student_mother_name, student_mothers_phone_no, student_email, student_phone_no, student_aadhar_number, student_nationality, student_religion, student_community, student_caste)
        )
        database.commit()

    return render_template('students_dashboard.html')




if __name__ == '__main__':
    app.run(debug=True)