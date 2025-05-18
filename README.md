Employment Management System - Employees DB

A Python-based Employment Management System to manage employee records with a simple database. This system supports basic operations: Add, Update, Delete, and Clear on employee records. The employee data includes details such as name, date of join, gender, address, age, email, and contact number.

🔍 Description

This system allows you to:
	•	Add Employee: Add new employee records with details such as name, date of join, gender, address, age, email, and contact number.
	•	Update Employee: Modify the details of an existing employee using their employee ID.
	•	Delete Employee: Remove an employee from the database.
	•	Clear Employees: Delete all employee records from the database.

The employee details are stored in a database with the following fields:
	•	Employee ID (unique identifier)
	•	Name
	•	Date of Join
	•	Gender
	•	Address
	•	Age
	•	Email
	•	Contact Number

Database Structure:
	•	Employee Table:
	•	id (Primary Key)
	•	name (VARCHAR)
	•	date_of_join (DATE)
	•	gender (VARCHAR)
	•	address (TEXT)
	•	age (INTEGER)
	•	email (VARCHAR)
	•	contact_number (VARCHAR)

⸻

🛠 Technologies Used
	•	Python – For backend logic and database interaction.
	•	SQLite/MySQL – For storing and managing employee records.
	•	SQLite3 library (or another database connector) – For database connectivity
