# class definition
class Student():
    def __init__(self):
        self.name = ""
        self.age = 0
        self.student_id = 0 #adding a third attribute

def main():
    # object creation based on the class
    student1 = Student()
    student2 = Student()
    student3 = Student() #adding a third student

    #Assign values ​​of all available attributes to all students:
    student1.name = "Dominic"
    student1.age = 19
    student1.student_id = 111111

    student2.name = "Olivia"
    student2.age = 21
    student2.student_id = 222222

    student3.name = "PeterPaker"
    student3.age = 20
    student3.student_id = 333333

    #print information about all students:
    print('LIST OF STUDENTS')
    print('================')
    print(f'{student1.name}, {student1.age} years old, student id: {student1.student_id}')
    print(f'{student2.name}, {student2.age} years old, student id: {student2.student_id}')
    print(f'{student3.name}, {student3.age} years old, student id: {student3.student_id}')


if __name__ == "__main__":
    main()