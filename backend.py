from flask import Flask, render_template, request, jsonify
import mysql.connector

# MySQL Credentials
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="01062006",
    database="college_db")

   #table="students_login"
   #     = "staffs_login"
   #     = "students_signup"
   #     = "staffs_signup"

cursor = conn.cursor()

app = Flask(__name__)

# Default
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/signin', methods=['POST'])
def signin_user():
    data = request.json
    user_type = data.get('type')  # student or staff
    email = data.get('email') if user_type == 'student' else data.get('username')  
    password = data.get('password')


#NEEDED TO BE CHANGED
    cursor.execute("INSERT INTO student_login (email, password) VALUES (%s, %s)", (email, password))
    conn.commit()
    '''user = cursor.fetchone()
    print(user)
    if user:
        return jsonify({"message": "Sign-in successful!"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401'''

# Signup
@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/signup.html', methods=['POST'])
def signup_user():
    data = request.json
    user_type = data.get('type')
    roll_no = data.get('Roll No')
    reg_no = data.get('Reg No')
    signup_email = data.get('Email')
    signup_password = data.get('Password')

#NEEDED TO BE CHANGED
    cursor.execute("INSERT INTO student_signup (roll_no, reg_no, email, password) VALUES (%s, %s, %s, %s)", (roll_no, reg_no, signup_email, signup_password))
    conn.commit()


# Login
@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_user():
    data = request.json
    user_type = data.get('type')
    signin_email = data.get('email')
    signin_password = data.get('password')
    
    cursor.execute("INSERT INTO students_login (email, password) VALUES (%s, %s)", (user_type,signin_email, signin_password))
    conn.commit()
    
    return jsonify({"message": "Sign-in successful!"})



if __name__ == '__main__':
    app.run(debug=True)
