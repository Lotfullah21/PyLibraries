class MyFirstClass:
    print("Who wrote this? ")
    index = "Author-Book"

    def hand_list(self, philosopher, book):
        print(MyFirstClass.index)
        return (f"{philosopher} wrote the book {book}")
    
whodunnit = MyFirstClass()
# print(whodunnit.hand_list("Plato","Enigma machine"))
print(dir(whodunnit))


# class MyClass:
#     a = "hello"
#     print("Hlleo")

# my = MyClass()
# print(my.a)


# class House:
#     num_bathrooms = 3
#     num_bedroom = 7

#     def __init__(self,rate):
#         pass

#     def cost_evaluation(self,rate):
#         cost = rate * self.num_bedroom + 0.5 * self.num_bathrooms
#         return cost
    
# house = House(12)
# print(house.cost_evaluation(3))
# print(house)





# class Recipe:
    
#     def __init__(self,dish,items, time):
#         self.dish = dish
#         self.items = items
#         self.time = time
    
#     def cook(self):
#         return f"{self.dish} has the {self.items} and takes {self.time} minutes to cook"
    
# Palaw = Recipe("Palaw",["oil","Rice","onion","tomato"],69)
# print(Palaw.cook())
