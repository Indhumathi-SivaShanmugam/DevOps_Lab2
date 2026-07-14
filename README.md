# DevOps_Lab2

Hi yall! this is a practice repo 
WE ARE doing this for learning! :)
<p align="center">
  <img src="https://png.pngtree.com/png-vector/20190223/ourmid/pngtree-student-glyph-black-icon-png-image_691145.jpg" width="150">
   <img src="https://images.scalebranding.com/modern-swinging-tree-logo-7ada1ffe-b54c-426f-905e-569ed6c5a38f.jpg" width="180">

 
 
</p>

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
