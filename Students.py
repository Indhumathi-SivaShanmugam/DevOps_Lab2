students = []

def add_student(name, mark):
    students.append({"name": name, "mark": mark})

def display_students():
    for student in students:
        print(student["name"], student["mark"])

def calculate_average(): total = sum(student["mark"] for student in students) return total / len(students)

def highest_mark():
    return max(students, key=lambda student: student["mark"])

print("STUDENT MARKS ANALYZER")
<<<<<<< HEAD


=======
print("Im making random changes")
>>>>>>> ad0045add74137b13a34e643331365d5c8bcf85f
