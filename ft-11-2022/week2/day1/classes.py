print("Hello World classes")
#functions
#boolean
#floats
#integers
#lists
#dictionary
#tuples() values that never change

#classes
#how you define a class in python


class Student:
    def __init__(self,name,age,ghusername):
        self.name = name
        self.age = age
        self.ghusername = ghusername

    def greeting(self):
        print(f"hello my name is {self.name}")
        print

vinny = Student("vinny",26,"VinnyVecchio")
joe = Student ("joe",20,"joef")
#dotnotation
print (vinny.age)
vinny.greeting()
    #name
    #age
    #github username