#Just normal print 1 to 10 using while loop
n = int(input("enter the value of n :"))
i=1
while(i<=10):
  print(n,"X",i,"=",(i*n))
  i+=1

li = [3,4,7,9,3,5,7] #it is a list
len = len(li) # to find the length of the list
idx =0 #starting point
while(idx<len-1):
  print(li[idx]) # print the index value the no.
  idx+=1


tup = (3,45,46,767,43,52,25,66,86,567)
findNo = int(input("Enter the value which you waant to find :")) # we find a no.

Index =0
while(Index<len(tup)):
  if(tup[Index]==findNo): # that is the condition
    print("This is the number -", Index)
    break #if we get this no. for one time then break it
  else:
    print("Do not into the tuple.")
  
  
  Index += 1


i=0
while(i<5):
  
  if(i==3):
    i+=1
    continue
  print(i)
  i+=1



#*FOR LOOP IN PYTHON*

num = [2,3,4,56,7,9] # it is a list
for i in num:  # i is the element of the given list
  print(i,end=" ")  # end is for print those value into a single line
  
  
name = "BRAINWARE UNIVERSITY"   #into the string we can print all individual charecter
for char in name :
  print(char)
else:
  print("NED")
  
  
 # find a perticular no. into a given list ? 
  
list = [2,3,4,5,6,7,8,9,65,34] # it is a normal list 
x =5 # it the value which we want to find (you take also it as user input )
idx =0  # It is for tracking the index value of that list
for ele in list:
  if(ele==x): # it is a normal condition
    print("Found",ele)
    break   #if we found the perticukar x value then break
  idx+=1  #it calculate the index
print(idx) # finally got the index



for i in range(5):
  print(i)
  i+=2
  
for i in range(1,10,1):   # first no. is for starting, 2nd no. is for length , and 3rd no. is for steps/increment or decrement
  print(i)
  
  
print("Even No.")
for i in range(1,10):
  print(i*2)


# multiplication table taking input from the user
n= int(input("Enter the value of n :"))

for i in range(1,10+1):
  print(n,"X",i,"=",i*n)
  
  
# if we do not want to work into the entier loop then we can used pass
for i in range(1,10):
  pass
print("Hello world")

num = int(input("Enter the value :"))
fact =1
for i in range(1,num+1):
  fact=fact*i
print(fact)