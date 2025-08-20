
# Finding percentage

number = float(input("Enter the value of the student number :"))

def stud_grade(number):
    if(number > 85):
        print("Grade -> A")
    elif(number>=75 and number<=85):
        print("Grade -> B")
    elif(number>=50 and number<=75):
        print("Grade -> c")
    elif(number>=30 and number<=50):
        print("Grade -> D")

    else:
        print("Fail")

stud_grade(number)

