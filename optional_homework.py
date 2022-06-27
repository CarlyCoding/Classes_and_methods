from logging import NOTSET

# Homework notes
# Optional exercise:
# - Create two classes, one called Instructor and one called Student- done 
# - The Instructor has a name of type string and a hobby and a Student has a name and a cohort . - done
# - The instructor also has a property called students which starts as an empty list.- done 
# - Create a method in instructor called add_student that receives a student object and adds it to the students list.- done
# - Create three instances: one of Instructor and two of Student.
# - Add to the Instructor object the two students (one by one), using the method add_student .
# - Draw class diagrams of both Instructor and Student (edited) 

class Instructor:
        def __init__(self, input_name, input_hobby):
            self.name = input_name
            self.hobby = input_hobby
            self.students = []

        def add_student(self, student):
            self.students.append(student)


class Student:
        def __init__(self, input_name, input_cohort):
            self.name = input_name
            self.cohort = input_cohort

# This is an instance of instuctors and students (Notes for revision)
instructor = Instructor("Steve", "Coding")
student = Student("Carly", "E59")
student2 = Student("Bella", "E59")

# Calling/Invoking function using lower case because using that specific instance of instructor. 
instructor.add_student(student)
instructor.add_student(student2)

print(instructor.students)




