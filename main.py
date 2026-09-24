from student_management import (
    students,
    add_student,
    update_student,
    search_student,
    view_students
)

from grade_calculator import (
    validate_marks,
    generate_performance_summary
)


def add_marks():
    """Add or update subject marks for a student."""

    student_id = input("Enter Student ID: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    subject = input("Enter Subject Name: ").strip()

    try:
        marks = float(input("Enter Marks (0-100): "))
    except ValueError:
        print("Invalid input. Marks must be a number.")
        return

    if not validate_marks(marks):
        print("Invalid marks. Marks must be between 0 and 100.")
        return

    students[student_id]["marks"][subject] = marks

    print(f"Marks for {subject} added successfully!")


def view_result():
    """Display the complete result of a student."""

    student_id = input("Enter Student ID: ").strip()

    if student_id not in students:
        print("Student not found.")
        return

    student = students[student_id]
    marks = student["marks"]

    if not marks:
        print("No marks available for this student.")
        return

    summary = generate_performance_summary(marks)

    print("\n========== STUDENT RESULT ==========")
    print(f"Student ID : {student_id}")
    print(f"Name       : {student['name']}")
    print(f"Course     : {student['course']}")

    print("\nSubject Marks:")
    for subject, mark in marks.items():
        print(f"{subject:<20} {mark}")

    print("\n------------------------------------")
    print(f"Total      : {summary['total']}")
    print(f"Percentage : {summary['percentage']}%")
    print(f"Grade      : {summary['grade']}")
    print(f"Result     : {summary['result']}")
    print(f"Performance: {summary['performance']}")
    print("====================================")


def main():
    """Main menu of the application."""

    while True:
        print("\n")
        print("=" * 45)
        print("   STUDENT RESULT & GRADE MANAGEMENT")
        print("=" * 45)

        print("1. Add Student")
        print("2. Update Student")
        print("3. Search Student")
        print("4. View All Students")
        print("5. Add / Update Marks")
        print("6. View Student Result")
        print("7. Exit")

        print("=" * 45)

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            update_student()

        elif choice == "3":
            search_student()

        elif choice == "4":
            view_students()

        elif choice == "5":
            add_marks()

        elif choice == "6":
            view_result()

        elif choice == "7":
            print("\nThank you for using the Student Result Management System!")
            break

        else:
            print("Invalid choice. Please select 1-7.")


if __name__ == "__main__":
    main()
