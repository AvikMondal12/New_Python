# Define the file name
filename = "note.txt"

# Open in read mode
f1 = open(filename, "r")
print("Read Mode:")
print("Name:", f1.name)
print("Mode:", f1.mode)
print("Closed:", f1.closed)
print("Readable:", f1.readable())
print("Writable:", f1.writable())
f1.close()
print("Closed after close():", f1.closed)
print()

# Open in write mode
f2 = open(filename, "w")
print("Write Mode:")
print("Name:", f2.name)
print("Mode:", f2.mode)
print("Closed:", f2.closed)
print("Readable:", f2.readable())
print("Writable:", f2.writable())
f2.close()
print("Closed after close():", f2.closed)
print()

# Open in append mode
f3 = open(filename, "a")
print("Append Mode:")
print("Name:", f3.name)
print("Mode:", f3.mode)
print("Closed:", f3.closed)
print("Readable:", f3.readable())
print("Writable:", f3.writable())
f3.close()
print("Closed after close():", f3.closed)
print()

# Open in read+write mode
f4 = open(filename, "r+")
print("Read+Write Mode:")
print("Name:", f4.name)
print("Mode:", f4.mode)
print("Closed:", f4.closed)
print("Readable:", f4.readable())
print("Writable:", f4.writable())
f4.close()
print("Closed after close():", f4.closed)
