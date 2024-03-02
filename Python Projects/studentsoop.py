class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

# Example usage
students = []

while True:
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = int(input("Enter student grade: "))
    student = Student(name, age, grade)
    students.append(student)

    choice = input("Do you want to add another student? (y/n): ")
    if choice.lower() == "n":
        break

for student in students:
    student.display()
