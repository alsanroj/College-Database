## 🏫 Student & Staff Portal – DBMS Mini Project

A simple, responsive web application built using **Flask** for backend and **HTML/CSS/JavaScript** for frontend, designed for managing student and staff sign-up and login operations. Developed as part of a Database Management System (DBMS) project.

---

## 👥 Contributors

<<<<<<< HEAD
- [Anish T](https://www.linkedin.com/in/anish-t)
- [Alsan Roj A](https://www.linkedin.com/in/alsan-roj-a-a01116295)
=======
- [Anish T](https://www.linkedin.com/in/anish-t) - Backend & Database
- [Alsan Roj A](https://www.linkedin.com/in/alsan-roj-a-a01116295) - Frontend
>>>>>>> 163f3b13538ea2dbe2c3daec483d90bb319ceca6

---

## 💻 Softwares Used

- `Frontend`
  - `HTML`
  - `CSS`
  - `JavaScript`

- `Backend`
  - `Python`

- `Database`
  - `MySQL`

- `API's`
  - `Cloud Flare` - Captcha:

---

## 📂 Project Structure

- `backend.py` – Main Flask backend with route handling.
- `college_db.sql` - Database Schema.
- `templates/` – HTML templates:
  - `Home.html`
  - `students_signup.html`
  - `staffs_signup.html`
  - `students_login.html`
  - `staffs_login.html`
  - `students_dashboard.html`
  - `staffs_dashboard.html`
- `static/`
  - `css/` – Stylesheets:
    - `Home.css`
    - `login.css`
    - `signup.css`
    - `students_dashboard.css`
  - `js/` – JavaScript files:
    - `home.js`
    - `login.js`
    - `signup.js`
  - `images/` – Assets like logos and background images:
  - `videos/` – Assets like animation and background videos:

---

## 🚀 How to Run

### 1. Clone the Repository (Terminal)
 
```bash
git clone https://github.com/alsanroj/College-Database.git
cd College-Database
```

### 2. Install Requirements (Terminal)

```bash
pip install flask pymysql cryptography
```

<<<<<<< HEAD
### 3. Run the Application (Terminal)
=======
### 3. Change the MySQL Database Credentials present in the Python Code (backend.py) to your MySQL Credentials.

Using MySQL Locally:
```bash
database = pymysql.connect(
    host="localhost",          # or "System IP Address"
    user="your username",      # or your MySQL username
    password="your password",  # use the password you set in MySQL
    database="college_db"      # your database name
)
```
(OR)

Using MySQL in Docker:
```bash
database = pymysql.connect(
    host="localhost",         # or "127.0.0.1"
    port=3306,                # use the port you mapped (default is 3306)
    user="root",              # or your MySQL username
    password="yourpassword",  # use the password you set in Docker
    database="college_db"     # your database name
)
```
(OR)

Using MySQL in a Server:
```bash
database = pymysql.connect(
    host="REMOTE SERVER IP ADDRESS OR HOSTNAME",  # e.g., "192.168.1.100" or "mysql.example.com"
    port=3306,                                    # default MySQL port, change if needed
    user="root",                                  # your MySQL username
    password="your_mysql_password",               # your MySQL password
    database="college_db"                         # your database name
)
```

### 4. Run the Application (Terminal)
>>>>>>> 163f3b13538ea2dbe2c3daec483d90bb319ceca6

```bash
python backend.py
```

<<<<<<< HEAD
### 4. Open in Browser
=======
### 5. Open in Browser
>>>>>>> 163f3b13538ea2dbe2c3daec483d90bb319ceca6
Navigate to: 
```bash
http://127.0.0.1:5000
```
(OR)
```bash
http://localhost:5000
```

---

## 🔧 Features

- **🎓 Student & 🧑‍🏫 Staff registration and login**

<<<<<<< HEAD
- **✨ Responsive UI using custom CSS**
=======
- **✨ Responsive UI using custom CSS and Bootstrap**
>>>>>>> 163f3b13538ea2dbe2c3daec483d90bb319ceca6

- **🎞️ Video background and interactive design**

- **📁 Flask-based routing and template rendering**

---

## 📜 Acknowledgements

Inspired by traditional university portals and built with simplicity and clarity in mind for better DBMS understanding.
