


students = [
    {"id": 101, "name": "Let's learn Python"},
    {"id": 102, "name": "Backend Development"},
    {"id": 103, "name": "Frontend Development"}
]


def find_student_by_id(student_id):
    student=None
    for i in students:
        if i['id']==student_id:
            student=i
    return student


try:
    user_input = int(input("Enter a student ID: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()

student = find_student_by_id(user_input)


if student:
    print("Student Found!")
    print(f"Student ID: {student['id']}")
    print(f"Student Name: {student['name']}")
else:
    print("Student not found.")
