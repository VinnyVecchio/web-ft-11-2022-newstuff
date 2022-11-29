#Ninja Turtles themed text rpg
#Developed by : Vincent Vecchio (Vinny)

#I pulled the theme/inspiration of my game from the early 1990’s cartoon series “Ninja Turtles”(one of my favorite cartoons when i was a child)
#  this was my first game i have built in python with my class at DigitalCrafts in Atlanta, GA.
#My game takes place in a sewer in NYC, as you go through passages to fight the Turtles from the series as the game progresses.
#  You will unlock pizza with every elimination and the passage will close. Eventually you will win by defeating all the turtles in the sewer, 
# now with all that said let me explain my logic on my thought process on how it was done

#Logic on how “Ninja Turtles” came together
#i started by making a character creation by asking the name of the player and connecting it to the class of Character with attributes tied to it like,
#  food[with a list] for storing your winnings, name, attack, and dodge. After that i made enemy attributes almost the same as the main character but no food, but slightly weaker but also tied to all 4 of the turtles.

#then came the storyline i outlined everything i wanted said when events happen depending on the path you decide to take. Each path will take you to fight a different Ninja Turtle,
#  then you will head back to camp automatically to then choose another path.

#Then came the difficult part for me the fighting mechanic of the game defining functions and tying the classes to interact in them.
#  then i added the food mechanic by creating a empty list tied to Character. and only had it put “pizza” in the list when one of the Turtles was killed. which could be eaten in the next battle to gain +25 hp to stay alive
#  to fight the upcoming turtles, but will reject your request if you do not have any food to eat.

#How did the collapse of the entrance work? well quite simple. a function to checked to see if the turtle that was on that path is alive or dead the boolean would return True or False 
# if they were alive or not if it came back True, you could walk the path and fight the turtle. but when defeated it would return false. Then shut the path

#What would i add if i had more time?
#If i had more time to really polish the game i would clean up the code in certain areas. 
# I would also add a weapon choice option at the beginning of the game to choose between a dagger, sword, mace ect... All coming with their own attributes. i would have also liked to add a shop buying feature. were maybe you can buy said weapons or more pizza for a upcoming boss battle(Master Splinter).Maybe a moves list tied to the weapon of choice that have their own attack damage and block attributes. The ideas go on forever.

#Will i expand on the game?
#I may expand on the game in future development. to add all of the features this project taught me allot about python as a whole. Understanding classes, functions, lists, variables, loops, methods, statements. 
# This Was definitely a learning experience and allot of fun doing it.





