class Person:
    def __init__(self,name, age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def intorduce(self):
        print(f"Hi my name is {self.name} and Im {self.age} years old")

    
class student(Person):
    def __init__(self,name, age,gender,student_id,grade):
        super().__init__(name, age,gender)
        self.student_id = student_id
        self.grade = grade

    def study(self):
        print(f"{self.name} is studying {self.grade} grade")

    def intorduce(self):
         super().intorduce()
         print(f"Im a student in grade {self.grade} and my student id is {self.student_id}")

  
class Teacher(Person):
    def __init__(self, name, age, gender,employee_id, subject):
        super().__init__(name, age, gender)
        self.employee_id = employee_id
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")

    def intorduce(self):
        super().intorduce()
        print(f"Im a teacher and I teach {self.subject} and my employeeId is {self.employee_id}")

    

obj_person = Person("Sri",24,"Male")
obj_person.intorduce()

print("\n")
obj_teacher = Teacher("Sathvik",24,"male",1234,"Python")
obj_teacher.intorduce()
print("\n")

obj_student = student("Prudhvi",24,"male",321,"12th")
obj_student.intorduce()