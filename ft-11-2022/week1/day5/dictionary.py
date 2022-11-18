#dictionary {"key": value}
# in order to get the value of a dictionary you need to klnow the key


pet = {"name": "fido"}
#print(pet["name"])
print (pet["name"])

michael = {"name": "mike"}
print(michael["name"])
print(michael["name"])


teacher = {"class": "math",
"classnumber": 213}

print(teacher["classnumber"])

print (facebookUser["bio"][-1]["i want you to print me"])

#  dictionary {"key": value}
# in order to get the value of a dictionary, you need to know the key

michael = {"name": "mike"}
print(michael["name"])

pet = {"name": "Fido", "height": "10ft"}
petsName = pet["name"]
print(pet["height"])


teacher = {"class": "math", "classNumber": 213}
print(teacher["classNumber"])
classNumber = teacher["classNumber"]
print(classNumber )











facebookUser = {
    "profilePic": "https://www.linkedin.com/feed/",
    "userName": "rokhayaisawesome",
    "firstName":"Rok",
    "lastName": "Haya",
    "bio":[
        "interest", "about me",
    {"story": [
        "well", 
        "this is really dumb", 
        "but", 
        [
            "I want you to print me"
            ]
            ]
        }
    ],
}
print(facebookUser["bio"][-1]["story"][-1][0])