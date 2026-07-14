students = []

def calculate_average(): total = sum(student["mark"] for student in students) return total / len(students)

print("STUDENT MARKS ANALYZER")