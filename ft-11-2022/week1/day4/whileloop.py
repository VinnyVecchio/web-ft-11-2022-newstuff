#while loop = execute some code while some condition remains true

name = input("enter your name")

while name == "":
    print("you did not enter your name")
    name = input("i said enter your name")

else:
    print("hello" + name)

age = int(input("enter your age "))

while age < 0:
    print("i said enter your age")
    age = int(input("enter it now"))

print (f"you are {age} years old")


food = input("enter a food you like (q to quit")

while not food == "q":
    print(f"you like {food}")
    food = input("enter another food you like (q to quit)")

print(f"oh you like {food} also")

num = int(input("enter a # between 1-10"))

while num < 1 or num > 10:
    print(f"{num} not valid")
    num = int(input("enter a # between 1-10"))

print(f"your {num} is not valid")

