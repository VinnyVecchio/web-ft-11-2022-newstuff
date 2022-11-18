largestNum = input("your number? \n")

array = range(1,int(largestNum)+1)

runningTot = 1
for num in array:
    runningTot = runningTot*num

print(runningTot)