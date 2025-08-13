# Distionaries are used to store data values in key:values pairs
#They are unordered,mutable(changes) & don't allow duplicates keys

dict ={
    "name":"Avik",
    "Age": 21,
    "subject" : ("Java", "Python","JavaScript"),  #can be use tuple
    "college":"Brainware University",
    "Stream":"BCA",
    "marks":[78,33,34,56] #can be use list
    
    # Can be apply here nested dictonary
    
}
print(dict)
dict["name"] = "Ramesh" # For change any value in the dictonary
print(dict)

print(dict.values()) # for print all the values

print(dict.items()) # print the whole dictonary 

print(dict.get("name")) #it is use because if the key is not available then it given none value .



#Nested Dictonary
dist ={
    "Name" : "Avik Mondal",
    "Score" :{
        "Math" : 89,
        "Phy" :57,
        "English" :56,
        "Computer" :67
    },
    
    "Subject":["Math","Eng","Geo","Edu","Phy"] # you can also store an array into the Dictonary
}

print(len(dist))  #if you find the length of the dictonary
print(dist.get("Subject"))  #To find a perticular value of an item 

print(dist.keys())   # In this case you return only just key that dictonary 
print(dist.values())  # In this case you return only just value of that perticular dictonary
print(dist.items())   # It is used to print the whole dictonary as well


print(dist.get("Name")) # in the get method if you give the wrong vlaue the also it give no error , it return only none . 
print(len(tuple(dist))) #also tuple and can possible
dist.update({"address":"Depara"})  #c If we want to update the dictonary that's why we can used it UPDATE method.
print(dist)





dictonary = {
    "cat" :"A small Animal",
    "table" :["A fun","facts and figure"]
}
print(dictonary)

emDict ={
    
}

sub1 = int(input("Enter the value of Phy"))
sub2 = int(input("Enter the value of Chme"))
sub3 = int(input("Enter the value of Math"))

emDict.update({"Phy" : sub1})
emDict.update({"Chme" : sub2})
emDict.update({"Math" : sub3})
print(emDict)