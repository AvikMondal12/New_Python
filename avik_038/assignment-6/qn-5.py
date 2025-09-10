#write the following using recursive functions.
#a. Fcatorial   b. nth fibonacci number    c.power calculation (x^n)


n = int(input("Enter the value of n : "))
def factoiral(n):
  if(n==1 or n==0):
    return 1
  return factoiral(n-1)*n

print(factoiral("Factorial : ",n))




#fibonacci
m = int(input("Enter the value of m : "))
def fibo(m):
  if m==0:
    return 0
  elif m==1:
    return 1
  else:
    return fibo(m-1)+ fibo(m-2)
  
print("Fibonacci  is :",fibo(m))


#Power Calculation
x = int(input("Enter the value of x : "))
y = int(input("Enter the value of y : "))
def cal_power(x,y):
  power = x**y
  print(f"Power of {x} and {y} is : {power}")

cal_power(x,y)