#pets make a class of pets
#def animalSound
class Pet:
    def __init__ (self,sound,kind):
        self.sound = sound
        self.kind = kind

    def greeting(self):
        print(f"i am a {self.kind}")


chicken = Pet("cluck", "chicken")

print(chicken.greeting())

#pets are going to be able to make a noise
#def animalSound()



#have an owner
#def whoIsMyOwner()



#have a name
#def whatsMyName()


#let us knopw what kind of pet they are
# def whatKindOfPet()

#what kind of pet is my task



class Pet:
    def __init__(self,sound,owner,name,kind):
        self.sound = sound
        self.owner = owner
        self.name = name
        self.kind = kind
    def whoIsMyOwner(self):
        print(f"my owner is {self.owner}")
    def sayMyName(self):
        print(f"my name is {self.name}")
    def whatKindOfPet(self):
        print(f"I am a {self.kind}")
    def animalSound(self):
        print(f"{self.sound}{self.sound}")

benji = Pet("hsssss","Amanda","Benji","Lizard")
Betsy = Pet("Moo","Farmer Joe","Betsy","Cow")

benji.sayMyName()
benji.whoIsMyOwner()
benji.whatKindOfPet()
benji.animalSound()

Betsy.sayMyName()
Betsy.whoIsMyOwner()
Betsy.whatKindOfPet()
Betsy.animalSound()