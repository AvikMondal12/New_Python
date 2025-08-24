number = float(input("Enter the number :"))

def stud_grd(number):
  if(number>85):
    print("Grade -> A")
    
  elif(number>=75 and 85>=number):
    print("Grade -> B")
  elif(number>=50 and 75>=number):
    print("Grade -> C")
  elif(number>=30 and 50>=number):
    print("Grade -> D")
  
  else:
    print("Fail")
    
stud_grd(number)