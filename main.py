from student import Student
from teacher import Teacher
from headmaster import Headmaster

def create_student():
    name = input("Enter student's name: ")
    age = int(input("Enter student's age: "))
    grade_level = int(input("Enter student's grade level: "))
    return Student(name, age, grade_level)

def create_teacher():
    name = input("Enter teacher's name: ")
    age = int(input("Enter teacher's age: "))
    subject = input("Enter teacher's subject: ")
    return Teacher(name, age, subject)

def create_headmaster():
    name = input("Enter headmaster's name: ")
    age = int(input("Enter headmaster's age: "))
    subject = input("Enter headmaster's subject: ")
    department = input("Enter headmaster's department: ")
    return Headmaster(name, age, subject, department)

def main():
    print("Welcome to the school management system!")
    student = create_student()
    teacher = create_teacher()
    headmaster = create_headmaster()

    print("\nActions:")
    print("1. Student study")
    print("2. Teacher teach")
    print("3. Headmaster manage department")
    action = int(input("Choose an action (1/2/3): "))

    if action == 1:
        student.study()
    elif action == 2:
        teacher.teach()
    elif action == 3:
        headmaster.manage_department()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()