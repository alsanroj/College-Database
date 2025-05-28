from flask import Flask,render_template,request,jsonify
import pymysql
import json
import time


app = Flask(__name__)

# Database connection
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
        cursor.execute("SELECT * FROM staffs WHERE roll_no=%s AND password=%s", (username, password))
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
        staff_firstname = request.form.get('staff_fName')
        staff_lastname = request.form.get('staff_lName')
        staff_email = request.form.get('staff_email')
        staff_phonenumber = request.form.get('staff_phNumber')
        staff_password = request.form.get('staff_password')
        staff_repassword = request.form.get('staff_rePassword')
        if staff_password != staff_repassword:
            error = "Passwords do not match"
            return render_template('staffs_signup.html', error=error)
        cursor.execute("SELECT * FROM staffs WHERE email=%s", (staff_email,))
        if cursor.fetchone():
            error = "Email already registered"
            return render_template('staffs_signup.html', error=error)
        cursor.execute(
            "INSERT INTO staffs (first_name, last_name, email, ph_number, password) VALUES (%s, %s, %s, %s, %s)",
            (staff_firstname, staff_lastname, staff_email, staff_phonenumber, staff_password)
        )
        database.commit()
        cursor.execute("SELECT * FROM staffs WHERE email=%s", (staff_email,))
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
        cursor.execute("SELECT * FROM students WHERE roll_no=%s AND password=%s", (username, password))
        student = cursor.fetchone()
        print(student)
        if student:
            return render_template('students_dashboard.html', student=student)
        else:
            error = "Invalid username or password"
            return render_template('students_login.html', error=error)
    return render_template('students_login.html')


# Students Signup
@app.route('/students_signup.html', methods=['GET', 'POST'])
def students_signup():
    if request.method == 'POST':
        student_firstname = request.form.get('student_fName')
        student_lastname = request.form.get('student_lName')
        student_email = request.form.get('student_email')
        student_phonenumber = request.form.get('student_phNumber')
        student_password = request.form.get('student_password')
        student_repassword = request.form.get('student_rePassword')
        if student_password != student_repassword:
            error = "Passwords do not match"
            return render_template('students_signup.html', error=error)
        cursor.execute("SELECT * FROM students WHERE email=%s", (student_email,))
        if cursor.fetchone():
            error = "Email already registered"
            return render_template('students_signup.html', error=error)
        cursor.execute(
            "INSERT INTO students (first_name, last_name, email, ph_number, password) VALUES (%s, %s, %s, %s, %s)",
            (student_firstname, student_lastname, student_email, student_phonenumber, student_password)
        )
        database.commit()
        cursor.execute("SELECT * FROM students WHERE email=%s", (student_email,))
        student = cursor.fetchone()
        print(student)
        if student:
            return render_template('students_dashboard.html', student=student)
        else:
            error = "An error occurred during registration"
            return render_template('students_login.html', error=error)
    return render_template('students_signup.html')



if __name__ == '__main__':
    app.run(debug=True)