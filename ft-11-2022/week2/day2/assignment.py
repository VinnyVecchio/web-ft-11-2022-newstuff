#Create a new file called "assignment.py" in your week2 day 2 folder
#Write all code beneath each question/problem
#

# 1. Write a function called "nameFunction" have it print out your name. invoke the function

#answer
#def nameFunction():
  #print("vinny")
#nameFunction()
        ##CODE GOES HERE FOR EACH uncommented

#2. Define variable named Joe that is the string Joe

#answer
#name = ("Joe")
#print(name)

#3 Reinitialize Joe so that it is now the integer 4

#Answer
#joe = 4
#print (joe)


#4 Change Joe into a float
#Answer
#joe = float (joe)
#print(joe)


#5. Create a list named students that includes 5 people from this class
students = ["vinny", "ethan", "rokhaya", "kenneth", "adam"]
    #5a print the first item from the list(bonus for more than one way)
#print(students[0])
    #5b print the last item from the list(bonus for more than one way)
#print(students[4])
#print(students[-1])
    #5c How do I get the third item from the list?
#students.pop(2)
#print(students)
   
    #5d print the entire list not in brackets [student1, student2, etc...]

#for names in students:
    #print(names, end= " ")
    #5e add "is cool" to the end of each name
    #iscool = ("is cool")
    #print (iscool)

    #5f if the students name is your name add "IT ME!!" to the end

#for student in range(len(students)):
    #if students[student] == 'vinny':
        #students[student] = 'IT ME!!'
#print(students)

    #5g if you are not in the list print "I guess I'm not cool"

    #5h list some methods to remove things from a list

#clear()
#pop()
#remove()
#del()

#6 Create a dictionary with keys "Digital Crafts" ,"Instructor", "TA" and values "Bootcamp" ,"Joe" ,"Ethan"
#Digital_crafts = {"digital crafts":"bootcamp", "instructor": "joe", "TA":"ethan",}
    #6a return the value of "Digital Crafts"
#print(Digital_crafts)


#7 Write a class named Cars with attributes make,model,year, and type(sedan,truck,crossover, sportscar, etc....)
class Cars:
    def __init__(self,make,model,year,type):
        self.make = make
        self.model = model
        self.year = year
        self.type = type
    #7a Instantiate 3 new Cars
    def corolla(self,make,model,year,type):
        print(corolla)

    def civic(self,make,model,year,type):
        print(civic)

    def taho(self,make,model,year,type):
        print(taho)
    
    def honkHorn(self):
        print("beep,beep")


taho = Cars("chevy","taho",2022,"suv")
corolla = Cars("toyota","corolla",2022,"sedan")
civic = Cars("honda","civic",2022,"sedan")
honkHorn = Cars.honkHorn()

    
    #7b Add a method that allows you to see the make and model of a car in your terminal
print(taho.type)
    #7c Use the above method on the second car
print(corolla.make)
    #7d Add a method that is called "honkHorn" that prints "Beep Beep"


#Push this all to a repo on your github
#Paste github link of assignment page to: https://digitalcrafts.instructure.com/courses/225/assignments/9345