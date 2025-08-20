
#find leap year
year = int(input("Enter he value of the year :"))

def leap_year(year):
    if(year%4==0 and (year%100 != 0 or year%400==0)):
        print("This is a leap year")
        return 
    else:
        print ("This is not a leap year")
        return
    
leap_year(year)

