students = {}


def add_student():
    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Student ID cannot be empty.")
        return

    if student_id in students:
        print("Student ID already exists.")
        return

    name = input("Enter Student Name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    try:
        age = int(input("Enter Age: "))

        if age <= 0 or age > 100:
            print("Age must be between 1 and 100.")
            return

    except ValueError:
        print("Invalid age. Please enter a number.")
        return

    course = input("Enter Course: ").strip()

    if not course:
        print("Course cannot be empty.")
        return

    students[student_id] = {
        "name": name,
        "age": age,
        "course": course,
        "marks": {}
    }

    print("Student added successfully!")


def update_student():
    student_id = input("Enter Student ID to update: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    name = input("Enter new name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    try:
        age = int(input("Enter new age: "))

        if age <= 0 or age > 100:
            print("Age must be between 1 and 100.")
            return

    except ValueError:
        print("Invalid age. Please enter a number.")
        return

    course = input("Enter new course: ").strip()

    if not course:
        print("Course cannot be empty.")
        return

    students[student_id]["name"] = name
    students[student_id]["age"] = age
    students[student_id]["course"] = course

    print("Student details updated successfully!")


def search_student():
    student_id = input("Enter Student ID to search: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]

    print("\n--- Student Details ---")
    print(f"Student ID : {student_id}")
    print(f"Name       : {student['name']}")
    print(f"Age        : {student['age']}")
    print(f"Course     : {student['course']}")
    print(f"Marks      : {student['marks']}")


def view_students():
    if not students:
        print("No student records available.")
        return

    print("\n--- All Student Records ---")

    for student_id, student in students.items():
        print(f"\nStudent ID : {student_id}")
        print(f"Name       : {student['name']}")
        print(f"Age        : {student['age']}")
        print(f"Course     : {student['course']}")
        print(f"Marks      : {student['marks']}")