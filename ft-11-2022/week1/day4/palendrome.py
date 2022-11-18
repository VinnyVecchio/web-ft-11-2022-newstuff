word = input ("enter a palindrate ")

counter = 1
ispalendrome = True
for letter in word:
    if letter != word[-counter]:
        ispalendrome = False
    counter = counter + 1
print(ispalendrome)