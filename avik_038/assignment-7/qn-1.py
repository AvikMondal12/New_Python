f = open("note.txt","w")
print("File create sucessfully")
f.write("Hello world by Avik")
f.close()


# B.
f = open("note.txt","r")
# f.write("Hello world by Avik")
print(f.read(10))
f.close()
print("File closed Sucessfully")



# C
f = open("note.txt","r")
print(f.read(10))
f.close()
print("File closed Sucessfully")
