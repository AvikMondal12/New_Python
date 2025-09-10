#Define a function for the area of a rectangle with a defult value for breadth

breadth = 10
length = int(input("Enter the value of the length :"))
def area_rectangle(length,breadth):
    area = (length*breadth)
    print(f"The area of the rectangle is :{area}")
    return
area_rectangle(length,breadth)