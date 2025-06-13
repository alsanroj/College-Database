-- Create the database
CREATE DATABASE IF NOT EXISTS college_db;
USE college_db;

-- Create the students table
CREATE TABLE IF NOT EXISTS students (
    roll_no VARCHAR(20) PRIMARY KEY,
    reg_no VARCHAR(20),
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    name VARCHAR(100),
    email VARCHAR(100),
    ph_number VARCHAR(20),
    password VARCHAR(50)
);

-- Insert sample data into students
INSERT INTO students (roll_no, reg_no, first_name, last_name, name, email, ph_number, password)
VALUES 
('23EE001', '312323105001', 'Aswin', 'A', NULL, 'aswin@sjce.com', '9447568589', 'sjce@123');

-- Create the staffs table
CREATE TABLE IF NOT EXISTS staffs (
    roll_no VARCHAR(20) PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    name VARCHAR(100),
    email VARCHAR(100),
    ph_number VARCHAR(20),
    password VARCHAR(50)
);

-- Insert sample data into staffs
INSERT INTO staffs (roll_no, first_name, last_name, name, email, ph_number, password)
VALUES 
('23ME789', 'Prakash', 'T', NULL, 'prakash@sjit.com', '6986754126', 'sjit@123');
