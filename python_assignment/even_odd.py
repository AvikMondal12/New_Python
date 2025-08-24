n = int(input("Enter the value of n :"))

def even_odd(n):
  if(n%2==0):
    return print(n,"-> is an Even Number")
  else:
    return print(n,"-> is an odd number")
even_odd(n)