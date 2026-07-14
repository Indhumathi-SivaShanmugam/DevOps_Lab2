students = []
def display_students():
    for student in students:
        print(student["name"], student["mark"])

print("STUDENT MARKS ANALYZER")



def highest_mark():
    return max(students, key=lambda student: student["mark"])


print("STUDENT MARKS ANALYZER")
print("Im making random changes")
