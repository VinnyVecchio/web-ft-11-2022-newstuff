#go through numbers and store it stock it at the end of the numbers

numbers = [1,2,5,0,7,0,9,0,2,0,2,3]
numbers.sort()
#print(numbers)

for num in numbers:
    if num == 0:
        # if its 0 remove the number im currently on 
      numbers.append(0)

print(num)



# newnew = "0"

#numbers.append(newnew)



#if num == 0:
#       while num < 1:
#           numbers.append(6)


#iterate through and find all the 0
#move all of the zeros to the back of the list
#then put them in order
