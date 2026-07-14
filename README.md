# DevOps_Lab2

Hi yall! this is a dummy repo 
WE ARE doing this for fun! :)


students = []


def add_student(name, mark):
    students.append({"name": name, "mark": mark})


def display_students():
    for student in students:
        print(student["name"], student["mark"])


def calculate_average():
    total = sum(student["mark"] for student in students)
    return total / len(students)


def highest_mark():
    return max(students, key=lambda student: student["mark"])


print("STUDENT MARKS ANALYZER")
