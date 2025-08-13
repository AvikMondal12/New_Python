a=int(input("Enter the value of first number :"))
b=int(input("Enter the value of second number :"))
c=int(input("Enter the value of third number :"))
d=int(input("Enter the value of fourth number :"))

if(a>b and a>c and a>d):
    print("First is largest number ",a)
elif(b>c and b>d):
    print("Second is the largest number ",b)
elif(c>d):
    print("Third is the largest numbe ",c)
else:
    print("Fourth is the largest number ",d)
    
num = int(input("Enter the value of the number :"))
if(num % 7 ==0):
    print(num ," is divisible by 7")
else:
    print(num,"is not divisible by 7")