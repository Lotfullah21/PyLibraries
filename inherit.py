
class Learner:
    def __init__(self,name):
        self.name = name

class Student(Learner):
    def __init__(self,name,area):
        super().__init__(name)
        self.area = area
    
    def __str__(self):
        return f"{self.name} is Larning about {self.area}"

class Professor(Learner):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject
    
    def __str__(self):
        return f"{self.name} is teaching about {self.subject}"
    
learner = Learner("Shrodinger")
student = Student("king","AI")
professor = Professor("Frank Rosenblat","Maths")
print(student)
print(professor)