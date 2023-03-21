class Animal:
    def __init__(self,age, name=None):
        self.age = age
        self.name = name
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def set_name(self, newAge):
        self.age = newAge
    def set_name(self, new_name):
        self.name = new_name

class Rabbit(Animal):
    tag = 1
    def __init__(self, age, parent1=None, parent2 = None):
        Animal.__init__(self,age)
        self.parent1 = parent1
        self.parent2 = parent2
        self.rid = Rabbit.tag
        Rabbit.tag = Rabbit.tag + 1
    
    def get_rid(self):
        return str(self.rid) + zfill(3)

    def get_parent1(self):
        return self.parent1

    def get_parent2(self):
        return self.parent2

    def __add__(self, other):
#               def __init__(self, age, parent1=None, parent2 = None):
        return Rabbit(0,self, other)

    
quick = Rabbit(2)
quick.set_name("small")
fat = Rabbit(4)
print(fat.name)
print(fat.age)
fat.set_name("big")
little_r = Rabbit(0,quick, fat)
little_r.set_name("naughty rabbit")
little_new = fat + quick
print(little_new.get_parent1())


# class Spell(object):
#     def __init__(self, incantation, name):
#         self.name = name
#         self.incantation = incantation

#     def __str__(self):
#         return self.name + ' ' + self.incantation + '\n' + self.getDescription()
              
#     def getDescription(self):
#         return 'No description'
    
#     def execute(self):
#         print(self.incantation)


# class Accio(Spell):
#     def __init__(self):
#         Spell.__init__(self, 'Accio', 'Summoning Charm')

# class Confundo(Spell):
#     def __init__(self):
#         Spell.__init__(self, 'Confundo', 'Confundus Charm')

#     def getDescription(self):
#         return 'Causes the victim to become confused and befuddled.'

# def studySpell(spell):
#     print(spell)

# spell = Accio()
# spell.execute()
# studySpell(spell)
# studySpell(Confundo())