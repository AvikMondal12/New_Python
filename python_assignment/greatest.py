number1 = float(input("Enter the value 1 :"))
number2 = float(input("Enter the value 2 :"))
number3 = float(input("Enter the value 3 :"))
def greatest(number1,number2,number3):
  if(number1>number2 and number1>number3):
    print(number1,"Is the greatest number.")
  elif(number2>number1 and number2>number3):
    print(number2,"Is the greatest number.")
  elif(number3>number1 and number3>number2):
    print(number3,"Is the greatest number.")
  else:
    print("Some numbers are eual")
greatest(number1,number2,number3)