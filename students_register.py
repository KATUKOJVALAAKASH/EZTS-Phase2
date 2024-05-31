student_details = {}
def add_student_details():
    for i in range(2):
        name = input("Enter student name: ")
        roll_number = input("Enter roll number: ")
        age = input("Enter age: ")
        student_details[name] = {
            "Roll Number": roll_number,
            "Age": age
        }
def access_student_details():
    name = input("Enter student name to access details: ")
    if name in student_details:
        print("Student Details:")
        print("Name:", name)
        print("Roll Number:", student_details[name]["Roll Number"])
        print("Age:", student_details[name]["Age"])
    else:
        print("Student not found.")
if __name__ == "__main__":
    add_student_details()
    access_student_details()