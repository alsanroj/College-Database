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
        try:
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

        except Exception as e:
            print("Error inserting data:", e)    

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
        cursor.execute("SELECT * FROM students WHERE BINARY rollno=%s AND BINARY password=%s", (username, password))
        student = cursor.fetchone()
        print(student)
        if student:
            session['student_logged_in'] = True  # Set session variable
            session['roll_no'] = username  # Optionally store roll_no
            return redirect(url_for('students_dashboard'))
        else:
            error = "Invalid username or password"
            return render_template('students_login.html', error=error)
    return render_template('students_login.html')




# Students Signup
@app.route('/students_signup.html', methods=['GET', 'POST'])
def students_signup():
    if request.method == 'POST':
        try:
            name = request.form.get('student_Name')
            rollno = request.form.get('student_Rollno')
            email = request.form.get('student_email')
            phonenumber = request.form.get('student_phNumber')
            password = request.form.get('student_password')
            repassword = request.form.get('student_rePassword')

            #Checks for valid role number
            if not rollno or not re.match(r'^\d{2}[A-Z]{2}\d{3}$', rollno):
                error = "Roll number must be in this format: Year of Admission , Department Name, Unique Number of the Student \n (e.g., 23EE271)"
                return render_template('students_signup.html', error=error)

            #Checks wheather the phone number is 10 digit ot not
            if not phonenumber or not re.match(r'^\d{10}$', phonenumber):
                error = "The Phone Number must contain 10 digits"
                return render_template('students_signup.html', error=error)

            #Checks for the password and re-password match
            if not password or len(password) < 16:
                error = "Password must contain at least 16 characters"
                return render_template('students_signup.html', error=error)
        
            if password != repassword:
                error = "Passwords do not match"
                return render_template('students_signup.html', error=error)

            #Checks for email duplicate
            cursor.execute("SELECT * FROM students WHERE email=%s", (email,))
            if cursor.fetchone():
                error = "Email already registered"
                return render_template('students_signup.html', error=error)

            #Inserts the new user (STUDENT) into the database
            cursor.execute(
                "INSERT INTO students (rollno, name, email, phone_number, password) VALUES (%s, %s, %s, %s, %s)",
                (rollno, name, email, phonenumber, password)
            )
            database.commit()
            cursor.execute("SELECT * FROM students WHERE email=%s", (email,))
            student = cursor.fetchone()
            print(student)
            if student:
                session['student_logged_in'] = True
                session['roll_no'] = rollno
                return redirect(url_for('students_dashboard'))
            else:
                error = "An error occurred during registration"
                return render_template('students_login.html', error=error)

        except Exception as e:
            print("Error inserting data:", e)

    return render_template('students_signup.html')




# Students Dashboard
@app.route('/students_dashboard.html', methods=['GET', 'POST'])
def students_dashboard():
    if not session.get('student_logged_in'):
        return redirect(url_for('students_login'))
    if request.method == 'POST':
        try:

            # Personal Details
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

            # Address Details
            local_address = request.form.get('local_address')
            permanent_address = request.form.get('permanent_address')
            city = request.form.get('city')
            taluk = request.form.get('taluka')
            district = request.form.get('district')

            # Admission Details
            college_name = request.form.get('institute_name')
            degree = request.form.get('degree')
            branch = request.form.get('branch')
            admission_batch = request.form.get('admission_batch')
            academic_year = request.form.get('academic_year')
            admission_date = request.form.get('admission_date')
            current_year = request.form.get('current_year')
            admission_type = request.form.get('admission_type')

            # Bank Details
            bank_name = request.form.get('bank_name')
            bank_account_number = request.form.get('bank_account_number')
            ifsc_code = request.form.get('ifsc_code')
            bank_address = request.form.get('bank_address')

        
            cursor.execute(
                "INSERT INTO student_personal_details (register_number, roll_no, name, gender, date_of_birth, father_name, father_mobile, mother_name, mother_mobile, mail, student_mobile, aadhar_number, nationality, religion, community, caste) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (student_register_number, student_roll_no, student_name, student_gender, student_dob, student_father_name, student_fathers_phone_no, student_mother_name, student_mothers_phone_no, student_email, student_phone_no, student_aadhar_number, student_nationality, student_religion, student_community, student_caste)
            )
            database.commit()

            cursor.execute(
                "INSERT INTO student_address_details (rollno, local_address, permanent_address, district, taluk, city) VALUES (%s, %s, %s, %s, %s, %s)",
                (student_roll_no, local_address, permanent_address, district, taluk, city)
            )
            database.commit()

            cursor.execute(
                "INSERT INTO student_admission_details (rollno, college_name, degree, branch, admission_batch, academic_year, admission_date, current_year, admission_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (student_roll_no, college_name, degree, branch, admission_batch, academic_year, admission_date, current_year, admission_type)
            )
            database.commit()

            print("Data Inserted Successfully")

        except Exception as e:
            print("Error inserting data:", e)

    return render_template('students_dashboard.html')




if __name__ == '__main__':
    app.run(debug=True)