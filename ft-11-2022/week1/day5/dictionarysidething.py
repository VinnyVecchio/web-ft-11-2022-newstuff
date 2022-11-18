phonebook_dict = { 'Alice': '703-493-1834', 'Bob': '857-384-1234', 'Elizabeth': '484-584-2923', "kareem": "938-489-1234" }

#1 
#print (phonebook_dict["Alice"])


#2
del phonebook_dict["Alice"]

3# change bobs phone number from phone book
#num = "857-384-4444"
#num = str.replace ("857-384-1234", "857-384-4444")
#print (num)

phonebook_dict ["Bob"] = "905-435-5344"
print(phonebook_dict)

for num in phonebook_dict.values():
    print(num)


#exersise 2

ramit = { 'name': 'Ramit', 'email': 'ramit@gmail.com', 'interests': 
    ['movies', 'tennis'], 'friends': 
    [ 
        { 'name': 'Jasmine', 'email': 'jasmine@yahoo.com', 'interests': 
            ['photography', 'tennis'] 
        }, 
        { 'name': 'Jan', 'email': 'jan@hotmail.com', 'interests': 
            ['movies', 'tv'] 
        }
    ] 
}

#Write a python expression that gets the email address of Ramit.

print(ramit["email"])

#Write a python expression that gets the first of Ramit's interests

print (ramit["interests"][0])

#Write a python expression that gets the email address of Jasmine.
print (ramit["friends"][0]["email"])

#Write a python expression that gets the second of Jan's two interests
print(ramit["friends"][1]["interests"][1])


#python letter_histogram.py Please enter a word: banana {'a': 3, 'b': 1, 'n': 2} In this exercise, are you using dynamic keys or fixed keys?
