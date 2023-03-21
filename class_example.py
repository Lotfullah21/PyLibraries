import datetime

class Person:
    def __init__(self,name):
        '''ínstantiate the data attributes'''
        self.name = name
        self.lastName = name.split(" ")[-1]
        self.birthday = None
    
    def getLastName(self):
        return self.lastName
    
    def setBirthday(self,month,day,year):
        self.birthday = datetime.date(year,month,day)
    
    def getAge(self):
        if self.birthday == None:
            raise ValueError
        else:
            (datetime.date.today() - self.birthday).days
    
    def __lt__(self,other):
        if self.lastName == other.lastName:
            if self.name < other.name:
                return True
            else:
                return False
        elif self.lastName < other.lastName:
            return True
        else:
            return False
    
    def __str__(self):
        return self.name
    



class NITPerson(Person):
    nextIdNum = 0
    def __init__(self,name):
        Person.__init__(self,name)
        self.idNum = NITPerson.nextIdNum
        NITPerson.nextIdNum +=1
    
    def getIdNum(self):
        return self.idNum
    def __lt__(self,other):
        if self.idNum < other.idNum:
            return True
        else:
            return False
    
    def speak(self,utternace):
        return (self.getLastName() +" Says" + utternace)
class Student(NITPerson):
    pass

class UG(Student):
    def __init__(self, name,classYear):
        Student.__init__(self, name)
        self.classYear = classYear

    def getClass(self):
        return self.classYear
    
    def speak(self, utternace):
        return Student.speak(self, " Dude " + utternace)
    
class Grad(Student):
    pass

def isStudent(obj):
    return isinstance(obj,Student)




p1 = Person("King")
p1.setBirthday(1,2,1998)

p2 = Person("King jr")
p2.setBirthday(1,2,1999)

p3 = Person("jani")
p3.setBirthday(1,2,2000)

people = [p1,p2,p3]
for p in people:
    print(p)

people.sort()
for p in people:
    print("sorted",p)


n1 = NITPerson("King")
n2 = NITPerson("Ali")
n3 = NITPerson("Ayaan")

nitians = [n1,n3,n2]
for n in nitians:
    print(n)

nitians.sort()
for x in nitians:
    print("sorted",x)

s1 = UG("Atiullah",2020)
s2 = UG("Attaulhaq",2021)
s3 = Grad("king")
print(s1)
print(s1.getClass())
print(s1.speak("When is the exam"))
print(s2.speak("Exam is on the 4th of march"))
print(isinstance(s1,UG))