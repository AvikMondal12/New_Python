# """"FUNCTION OF PYTHON """



# def calSum (a,b,c):
#   sum=(a+b+c)
#   print(sum)
#   return sum
# calSum(2,4,3)
# calSum(6,7,4)



#   # it is different type of rules to write functon in the python 
# def sum (a,b):
#   return a+b

# n=sum(2,3)
# print(n)

# # avagrage of three number using function

# def avarage(a,b,c):

#   avg = (a+b+c)/3
#   print(avg)
#   return avg

# a = int(input("Enter the value of a :"))
# b = int(input("Enter the value of b :"))
# c = int(input("Enter the value of c :"))

# avarage(a,b,c)


# def cal_mul(a=2,b=2):
#   multi = a*b
#   print(multi)
#   return multi

# cal_mul(4,4)


# list = [3,4,5,7,8,1]
# def list_len(li):
  
#   print(li)
#   return li

# list_len(list)
  
  
  
#   # factorial using function 
  
# n =int(input("Enter the value of n :"))


# def factorial(n):
#   fact = 1
#   for i in range(1,n+1):
#     fact= fact*i
#   print(fact)
   
# factorial(n)

# # USD to INR conerter

# usd = int(input("Enter the value of usd :"))

# def converter (usd):
#   inr = float(input("Enter the value of INR :"))
#   con_inr = usd*inr
#   print(con_inr)
#   return con_inr

# converter(usd)


# # CHECKING ODD ENVEN USING FUNCTION 

# n = int(input("Enter the value of n :"))

# def cal(n):
#   for i in range(n):
#     if(i%2==0):
#       print(i,"Even")
#     else:
#       print(i,"Odd")
#   return cal
# cal(n)



# # Recursive function

# n= int(input("Enter the value of n :"))

# def show(n):
#   if(n==0):
#    return
#   print(n)
#   show(n-1)

# show(n)



# # Factorial using recursive function

# n = int(input("enter the value of n :"))

# def factorial(n):
#   if(n==0 or n==1):
#     return 1
  
#   return factorial(n-1)*n
# print(factorial(n))


# def calSum(n):

#   if(n==0):
#     return 0
 
#   return calSum(n-1)+n
# print(calSum(3))
n = int(input("Enter the value of n : "))
def factoiral(n):
  if(n==1 or n==0):
    return 1
  return factoiral(n-1)*n

print(factoiral(n))