# Step 1: Create a class
class Student:
    
# Step 2: Initialize the student
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
    
 #Method to display student details
    def display_info(self):
        print("\n" + "="*45)
        print(f"{'--- STUDENT PROFILE ---':^45}")
        print("="*45)
        print(f"{'Name':<15} : {self.name}")
        print(f"{'Roll number':<15} : {self.roll}")
        print(f"{'Marks':<15} : {self.marks}")

# Method to check result
    def check_result(self):
        if self.marks >= 40:
            print("\nResult: PASS" )
            print('='*45)
        else:
            print("\nResult: FAIL")
            print('='*45)
print('='*45)
# Take input from user
name = input("Enter student name: ")
roll = int(input("Enter roll number: "))
marks = int(input("Enter marks: "))

# Create Student object
student1 = Student(name, roll, marks)

#Call methods
student1.display_info()
student1.check_result()
