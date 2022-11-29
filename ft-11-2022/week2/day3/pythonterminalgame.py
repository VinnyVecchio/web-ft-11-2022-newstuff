#create a class for my character[]
#good character and bad character ninja turtles
#weapon choice axe,hammer,sword)[]
#MUST HAVE ATTACK DAMAGE 10[]
#MUST BE ABLE TO CHOOSE THE NAME OF THE CHARACTER[]
#show stats after of character[]
#be able to fight villians 3? chosen 1, 2, 3[]
#run away function or if reaching 0 hp[]
#[]

from time import sleep

def stars():
    print('************************************************')
    sleep(2)
def printTurtleArt():
    print("""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⡀⠀⠀⠀⠀⢠⣤⣄⠀⣀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣴⠟⠛⠉⠁⠀⠀⠈⠉⠛⠻⣦⣄⠀⢸⡟⠙⣿⡟⣷⡀
⠀⠀⠀⠀⠀⢠⣾⠏⠁⣀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡈⠻⣷⣼⣧⠀⢹⡇⣹⡇
⠀⠀⠀⠀⣰⡿⠟⠛⢛⣛⣛⡿⢶⣶⣶⡶⢿⣛⣛⡛⠛⠿⢿⣿⣷⣿⣣⡿⠁
⠀⠀⠀⠀⣿⠁⢀⣼⠟⣯⣝⣻⣦⣤⣤⣾⣟⣫⣭⠻⣷⡄⠈⣿⣨⣿⠋⠀⠀
⠀⠀⣠⡾⠻⢷⣬⣛⣿⡿⠟⠋⠁⠀⠀⠈⠉⠛⢿⣿⣋⣵⡾⠛⢿⣅⠀⠀⠀
⠀⣼⠟⠀⠀⠀⠉⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠁⠀⠀⠀⠻⣧⠀⠀
⠰⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠆⠀
⠀⢻⣦⠀⠀⠀⠀⠀⢴⣤⣤⣀⣀⠀⠀⣀⣠⣤⡾⢿⡆⠀⠀⠀⠀⣴⡟⠀⠀
⠀⠀⠙⢷⣤⣀⠀⠀⠀⠈⠉⠙⠛⠛⠛⠛⠉⠁⠀⠈⠁⠀⣀⣤⡾⠋⠀⠀⠀
⠀⠀⠀⠀⠈⠛⠷⢶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠟⠋⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠛⢷⣤⣀⡀⠀⠀⢀⣠⣴⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀


    """)

class Character():
    def __init__(self,name):
        self.food = []
        self.name = name
        self.health = 100
        self.attack = 10
        self.dodge = 5
       
    def playerAttack(self, enemy):
        playerAttack = self.attack - enemy.dodge
        enemy.health -= playerAttack
        if enemy.health > 0 :
            print(f"{enemy.name} new health is {enemy.health}")
        else:
            sleep(2)
            print(f"{enemy.name} dies")
            stars()
            enemy.alive = False
            print("you picked up a slice of pizza")
            stars()
            sleep(3)
            self.food.append("pizza")
            print(self.food)
    def eatFood(self):
        if self.food == []:
            print("you got no pizza to eat!")
        else:
            print("you eat a slice of pizza")
            self.health += 25
            print(f"your new health is {self.health}")
            self.food.pop(0)

    

class Turtles():
    def __init__(self,name):
        self.name = name
        self.health = 50
        self.attack = 10
        self.dodge = 2
        self.alive = True
    def enemyAttack(self, playerName):
        Attack = self.attack - playerName.dodge
        playerName.health -= Attack
        if playerName.health > 0 :
            print(f"{playerName.name} new health is {playerName.health}")
        else:
            print(f"{playerName.name} dies")

Michaelangelo = Turtles("Michaelangelo")
Raphael = Turtles("Raphael")
Donatello = Turtles("Donatello")
Leonardo = Turtles("Leonardo")



def fightMenu(badTurtle):
    while badTurtle.health > 0 and playerName.health > 0:


        playerChoice = input( """
 Choose what to do input 1 - 3
   ("1. swing ")
    ("2. block ")
    ("3. flee ")
    ("4. eat some pizza")

--> """)
        if playerChoice == "1":
            
            print("you swing! ")
            playerName.playerAttack(badTurtle)
            badTurtle.enemyAttack(playerName)

        elif playerChoice == "2":
            print("""you throw up your dagger up in defence, 

                *CLINK* 
        
            it worked!!
            
            """)
        elif playerChoice == "3":
            print("you run back to safety of camp")
            homeCamp()
        elif playerChoice == "4":
            playerName.eatFood()
        else:
            print("please only type 1-4")

    homeCamp()


def mainMenu():
    printTurtleArt()
    print("""  
    ***********************
    *******SEWER SLAYER*******
    ***********************
    """)
    
def firstbattle():
            print("""

            you see 1... TURTLE?????
            this could only mean one thing
            your in New York City and your sences were right
            it is pizza you pull the dagger now its your time

                    (Michelangelo leaps)
                        **smash**
                    He hits your dagger

            """) 

def northBattle():
    print("""

      __O
     / /\_,               
   ___/\                  
       /_                 
--------------------------------

        you walk north from home camp you see a purple mask and a staff in the shadows
        you know from your previous run in it has to be Donatello you gear up for battle
        once more

""")
    badTurtle = Donatello
    fightMenu(badTurtle)


def southBattle():
    print("""

      __O
     / /\_,               
   ___/\                  
       /_                 
--------------------------------

        you walk south from home camp you see a red mask and a daggers in the shadows
        you know from your previous run in it has to be Raphael you gear up for battle
        once more

""")
    badTurtle = Raphael
    fightMenu(badTurtle)

def eastBattle():
    print("""

      __O
     / /\_,               
   ___/\                  
       /_                 
--------------------------------

        you walk east from home camp you see a blue mask and swords in the shadows
        you know from your previous run in it has to be Leonardo you gear up for battle
        once more

""")
    badTurtle = Leonardo
    fightMenu(badTurtle)

def homeCamp():
    fightDirection = input(""""you walk to camp to rest up, in camp you figure out another direction to take 
there is only 3 other ways to take north, south, and east but what do you choose
1. north
2. south
3. east
 """)
    if fightDirection == "1":
        if Donatello.alive == True:
            northBattle()
        else:
            print("the passage seems to be blocked. you wander back to camp")
            homeCamp()
    elif fightDirection == "2":
        if Raphael.alive == True:
            southBattle()
        else:
            print("The passage is now shut.")
            homeCamp()
    elif fightDirection == "3":
        if Leonardo.alive == True:
            eastBattle()
        else:
            print("")
            homeCamp()


def startGame():
    print (f"""
                    
        _(:ι」∠)_  

       {playerOne} you wake in a haze, your in a sewer, but what sewer?
        what city? why does it smell so rancid,almost smells like...
        pizza. old pizza maybe... somthing is in your arm. a small dagger
        you pull it out. and put it in your pocket you might need it for later.
        you check your surroundings and realize there is 4 paths
        north, south, east, west
        
        """)
playerOne = input ("""

ס₪₪₪₪§|(ΞΞΞΞΞΞΞΞΞΞΞ> what is your fighters name ס₪₪₪₪§|(ΞΞΞΞΞΞΞΞΞΞΞ>\n""")
playerName = Character(playerOne)
mainMenu()
gameStart = input("Welcome to sewer slayer would you like to play the game (yes? or no?)\n")
if gameStart == ("yes"):
    startGame()
elif gameStart == ("no"):
    mainMenu()
else:
    print("please type only yes or no")

firstDirection = input("but what side do you take right or left >> ")
if firstDirection == "right":
    badTurtle = Michaelangelo
    firstbattle()
if firstDirection == "left":
    badTurtle = Michaelangelo
    firstbattle()    
    
fightMenu(badTurtle)


