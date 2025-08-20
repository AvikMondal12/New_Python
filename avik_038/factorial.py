n = int(input("Enter the value of n :"))

def factorial(n):
    if(n==0 or n==1):
        return 1
    return factorial(n-1)*n
print(factorial(n))


#or
fact = 1
i=1
while i<=n:
    fact=i*fact
    i+=1
print(fact)