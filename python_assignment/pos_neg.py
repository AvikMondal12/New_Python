number = float(input("Enter the value of the number :"))

def pos_neg(number):
  if(number==0):
    print(number,"-> It is Zero")
  elif(number>0):
    print(number,"-> It is a possitive number.")
  elif(number<0):
    print(number,"-> It is an negtive number")
  else:
    print("please , Enter the valid numebr")
    
pos_neg(number)