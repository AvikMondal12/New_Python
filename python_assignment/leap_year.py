year = int(input("Enter the value of the year :"))

def leap_year(year):
  if(year%4==0 and (year%100!=0 or year%400==0)):
    print(year,"-> This year is a leap year")
    
  else:
    print(year, "-> This year is not a leap year")
    
leap_year(year)