# Student Result & Grade Management System

A Python-based Command-Line Interface (CLI) application developed as part of the VEDA Technology Internship.

The system allows users to manage student records, subject marks, grades, percentages, PASS/FAIL results, and academic performance levels.

---

## 🎯 Objectives

- Manage student information efficiently.
- Add and update student records.
- Store subject-wise marks.
- Calculate total marks and percentage automatically.
- Assign grades based on percentage.
- Determine PASS/FAIL status.
- Provide academic performance classification.
- Validate user input and handle invalid data.
- Maintain a modular and maintainable Python codebase.

---

## 🚀 Features

### Student Management
- Add Student
- Update Student
- Search Student
- View All Students

### Marks Management
- Add subject marks
- Update existing marks
- Validate marks between 0 and 100

### Result Management
- Calculate total marks
- Calculate percentage
- Automatically assign grade
- Determine PASS/FAIL
- Display performance level

### Input Validation
- Empty Student ID validation
- Duplicate Student ID detection
- Student name validation
- Age validation
- Course validation
- Marks validation
- Invalid numerical input handling

---

## 📊 Grading System

| Percentage | Grade |
|------------|-------|
| 90–100 | A+ |
| 80–89 | A |
| 70–79 | B |
| 60–69 | C |
| 50–59 | D |
| 40–49 | E |
| Below 40 | F |

### Result

- Percentage ≥ 40 → PASS
- Percentage < 40 → FAIL

### Performance Levels

| Percentage | Performance |
|------------|-------------|
| 90+ | Outstanding |
| 80–89 | Excellent |
| 70–79 | Very Good |
| 60–69 | Good |
| 50–59 | Average |
| 40–49 | Needs Improvement |
| Below 40 | Poor |

---

## 🛠️ Technologies Used

- Python
- Python Dictionaries
- Functions
- Exception Handling
- Git
- GitHub
- PowerShell

The project uses only Python's standard library and does not require external packages.

---

## 📁 Project Structure

```text
student-result-grade-management/
│
├── main.py
├── student_management.py
├── grade_calculator.py
├── README.md
├── requirements.txt
├── .gitignore
└── screenshots/
File Description
File	Description
main.py	Main application and menu
student_management.py	Student record operations
grade_calculator.py	Marks, percentage, grade and result calculations
README.md	Project documentation
requirements.txt	Python dependencies
.gitignore	Files excluded from Git
▶️ How to Run
1. Clone the repository
git clone https://github.com/Mahima2005-shetty/student-result-management-system.git
2. Navigate to the project
cd student-result-management-system
3. Run the application
python main.py
🖥️ Application Menu
=============================================
   STUDENT RESULT & GRADE MANAGEMENT
=============================================
1. Add Student
2. Update Student
3. Search Student
4. View All Students
5. Add / Update Marks
6. View Student Result
7. Exit
=============================================
🧮 Sample Result

Example marks:

Subject	Marks
Python	85
DBMS	78
Java	92

Output:

========== STUDENT RESULT ==========
Student ID : S001
Name       : Student Name
Course     : Information Science

Subject Marks:
Python               85.0
DBMS                 78.0
Java                 92.0

------------------------------------
Total      : 255.0
Percentage : 85.0%
Grade      : A
Result     : PASS
Performance: Excellent
====================================
🧪 Testing

The application was tested for:

Valid student registration
Duplicate Student ID
Empty Student ID
Empty student name
Invalid age
Empty course
Valid marks
Marks below 0
Marks above 100
Non-numeric marks
Student search
Result calculation
Grade calculation
PASS/FAIL calculation
Performance classification

Python syntax validation was performed using:

python -m py_compile main.py student_management.py grade_calculator.py
🔐 Validation & Error Handling

The application uses validation and exception handling to prevent invalid input.

Examples:

Student ID cannot be empty.
Student ID already exists.
Student name cannot be empty.
Age must be between 1 and 100.
Invalid age. Please enter a number.
Invalid marks. Marks must be between 0 and 100.
Student not found.
🔮 Future Enhancements

Future versions can include:

SQLite/MySQL database integration
Persistent student records
Delete student functionality
PDF result generation
CSV/Excel export
Student login system
Role-based access
Attendance management
Graphical User Interface
Student performance analytics
📌 Project Information

Project: Student Result & Grade Management System
Internship: VEDA Technology Internship
Day: Day 1
Language: Python
Application: CLI
Version Control: Git
Repository: GitHub

👩‍💻 Author

Mahima M

GitHub:
https://github.com/Mahima2005-shetty

📄 License

This project was developed for educational and internship purposes.
