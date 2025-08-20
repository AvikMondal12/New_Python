
# Find greatest number among threee number 
x = int(input("Enter the value of num 1:"))
y = int(input("Enter the value of num 2:"))
z = int(input("Enter the value of num 3:"))
def greatest(x,y,z):
    if(x>y and x>z):
        print("Number 1 is the greatest number.")
        return x
        
    elif(y>x and y>z):
        print("Number 2 is the greatest number.")
        return y
    else:
        print("Number 3 is the greatest number.")
        return z 
    
greatest(x,y,z)
