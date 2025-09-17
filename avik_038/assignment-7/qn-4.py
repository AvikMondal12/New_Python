# Step 1: Create and write to the file
with open("pointer.txt", "w") as f:
    f.write("Avik, 85\nManish, 90\nkuntal, 78\nSuman, 98")

# Step 2: Read and demonstrate tell() and seek()
with open("pointer.txt", "r") as f:
    print("Initial pointer position:", f.tell())  # Should be 0

    # Read first 10 characters
    data = f.read(10)
    print("Data read:", data)
    print("Pointer after reading 10 chars:", f.tell())

    # Move pointer back to beginning
    f.seek(0)
    print("Pointer after seek(0):", f.tell())

    # Read full content
    full_data = f.read()
    print("Full content:\n", full_data)

    # Move pointer to position 6 and read from there
    f.seek(6)
    print("Pointer moved to position 6:", f.tell())
    print("Data from position 6:", f.read(10))
