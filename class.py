
class Student:
    # self creates objects inside the empty objects
    def __init__(self, name, house,rank="90"):
        if not name:
            raise ValueError("Missing name")
        if house == "" or house not in ["baghlan","khost","jntuh","afg"]:
            raise ValueError("Not a valid house")
        self.name = name
        self.house = house
        self.rank = rank
    
    def __str__(self):
        return f"{self.name} is from {self.house}"
    # it is a function that allows us to write our programs more defencively
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house == "" or house not in ["baghlan","khost","jntuh","afg"]:
            raise ValueError("Not a valid house")
        # we cannot have the same variable name as functions
        self._house = house
    
    def country(self):
        if self.house == "afg":
            return "Afghanistan"
        
    @classmethod
    def get(cls):
        name = input("Name")
        house = input("House")
        return cls(name, house)
        
def main():
    student = Student.get()
    print(student)



    
if __name__ == "__main__":
    main()















# class Student:
#     # self creates objects inside the empty objects
#     def __init__(self, name, house,rank="90"):
#         if not name:
#             raise ValueError("Missing name")
#         if house == "" or house not in ["baghlan","khost","jntuh","afg"]:
#             raise ValueError("Not a valid house")
#         self.name = name
#         self.house = house
#         self.rank = rank
    
#     def __str__(self):
#         return f"{self.name} is from {self.house}"
#     # it is a function that allows us to write our programs more defencively
#     @property
#     def house(self):
#         return self._house
    
#     @house.setter
#     def house(self, house):
#         if house == "" or house not in ["baghlan","khost","jntuh","afg"]:
#             raise ValueError("Not a valid house")
#         # we cannot have the same variable name as functions
#         self._house = house
    
#     def country(self):
#         if self.house == "afg":
#             return "Afghanistan"
        
# def main():
#     student = get_student()
#     print(student)
#     print(student.country())


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     rank = (input("Rank: "))
#     student =  Student(name, house,rank)
#     return student


















# class Student:
#     # self creates objects inside the empty objects
#     def __init__(self, name, house,rank):
#         if not name:
#             raise ValueError("Missing name")
#         if house == "" or house not in ["baghlan","khost","jntuh"]:
#             raise ValueError("Not a valid house")
#         self.name = name
#         self.house = house
#         self.rank = rank

# def main():
#     student = get_student()
#     print(student.name,"is from",student.house, "he got",student.rank,"rank")

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     rank = int(input("Rank: "))
#     return  Student(name, house,rank)
    
    

# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student




# def get_name():
#     return input("Name: ")

# def get_house():
#     return input("House: ")


# if __name__ == "__main__":
#     main()