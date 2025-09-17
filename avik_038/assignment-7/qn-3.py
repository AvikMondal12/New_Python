# Step 1: Create the file (if it doesn't exist)
open("student.txt", "a").close()  # This ensures the file exists without overwriting

# Step 2 & 3: Add student records and append without overwriting
while True:
    name = input("Enter student name: ")
    marks = input("Enter student marks: ")

    with open("student.txt", "a") as f:
        f.write(f"{name}, {marks}\n")

    more = input("Add another student? (yes/no): ").strip().lower()
    if more != "yes":
        break

print("All student records saved to student.txt.")
