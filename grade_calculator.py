def validate_marks(marks):
    """Validate marks between 0 and 100."""
    return 0 <= marks <= 100


def calculate_total(marks):
    """Calculate total marks."""
    return sum(marks.values())


def calculate_percentage(marks):
    """Calculate percentage."""
    if not marks:
        return 0

    total = calculate_total(marks)
    maximum_marks = len(marks) * 100

    return (total / maximum_marks) * 100


def calculate_grade(percentage):
    """Assign grade based on percentage."""
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 40:
        return "E"
    else:
        return "F"


def get_result(percentage):
    """Determine pass or fail."""
    return "PASS" if percentage >= 40 else "FAIL"


def get_performance_level(percentage):
    """Provide a descriptive performance level."""
    if percentage >= 90:
        return "Outstanding"
    elif percentage >= 80:
        return "Excellent"
    elif percentage >= 70:
        return "Very Good"
    elif percentage >= 60:
        return "Good"
    elif percentage >= 50:
        return "Average"
    elif percentage >= 40:
        return "Needs Improvement"
    else:
        return "Poor"


def generate_performance_summary(marks):
    """Generate complete academic performance summary."""

    total = calculate_total(marks)
    percentage = calculate_percentage(marks)
    grade = calculate_grade(percentage)
    result = get_result(percentage)
    performance = get_performance_level(percentage)

    return {
        "total": total,
        "percentage": round(percentage, 2),
        "grade": grade,
        "result": result,
        "performance": performance
    }