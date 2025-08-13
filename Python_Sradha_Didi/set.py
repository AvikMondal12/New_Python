""" 

 ***   "We can't store any MUTUBLE value like dictonary and list ."
 Otherwise we can store any value like int,float, tuple, str
 
"""


set3 = {1,2,3,4,4,"Avik","Sourav","Avik",4}   # In this case set alaways return unique value , it igenore duplicate value .

print(set3) # when it gives output it doesn't follow any order
print(type(set3))
print(len(set3))
# print(set3.clear())  To remove all the whole set


set2 = set() # to create an empty set

num1= int(input("Enter the value of No.1 :"))
num2= int(input("Enter the value of No.2 :"))
num3= int(input("Enter the value of No.3 :"))
set2.add(num1)
set2.add(num2)
set2.add(num3)
print(set2)

print(len(set2))





set ={"Rakesh","Avik","Dev","Sham","Abhi"}
print(set.pop()) #Pop is used to remove a random value into a set



# for union of 2 sets
set1 ={2,1,3}
set2= {3,4,5}
print(set1.union(set2))

print(set1.intersection(set2))  # to return the common value of those sets



subjects ={
  "java","python","C++","JS","java","python","java","C++","c"
  }
print(subjects)
print(len(subjects))


set5 = {
  ("int",9),("float",9.0)
}
print(set5)