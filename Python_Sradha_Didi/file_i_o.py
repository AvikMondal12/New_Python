# f = open("note.txt","r")
# print(f.read())   # for just read a file into any path
# print(type(f))
# f.close()


# print(f.read(10))  # that arguments is use for how many character we want to read 

# print(f.readline())  # this is used for read a perticular line ,and it's alaways take the first line as the by deafult value



# Writing to a file .
f= open("demo.txt","a")
f.write("\n ok bye now")

f.close()


# to delete a fie into pyhton 
# import os 
# os.remove("demo.txt")   