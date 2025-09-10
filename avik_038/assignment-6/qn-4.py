# Write a function that returns both sum and product of two given numbers.

n = float(input("Enter the value of n :"))
m = float(input("Enter the value of m : "))
def sum_pro(n,m):
    return n+m,n*m
x = sum_pro(n,m)
print(f"Sum : {x[0]}, Product : {x[1]}")

