sub = (1,"Python",2,"Java",3,"C",4,"Rubi",5,"C++")




print(sub)# print the tuple
print(sub.index("Java")) #index method of the tuple
print(sub.count("Java"))#count method of the element 

print(sub[5]) #access element by index
sing_tup = (5,)#single element tuple
print(sing_tup)
nstd_tup=(1,(1,2),2,(3,4),3,(4,5)) # nested tuple
print(nstd_tup)

# Tuple unpacking
unpck_tup = (1,2,3) # this is the tuple unpaking
x,y,z = unpck_tup
print(x)
print(y)
print(z)



print("\n THIS OUTPUT IS FOR SET\n")

set = {sub} # Duplicate of tuple 
set.add(".net") # add method in set

print(set) # print the set

set.remove(".net") # remove element of set
print(set) # print the set


set_1 = {1,6,9,4}
set_2={4,5,6}
print(set_1.union(set_2))  # union with set-1 and set-2
print(set_1.intersection(set_2)) # intersection with set-1 and set-2
print(set_1.difference(set_2)) # Defference between set-1 and set-2
print(set_1)

#Squre of element which element is divisible by 3 
for i in set_1:
  if(i%3==0):
    print("This element is divisible by 3 :",i)
    print("Squre of ,",i,"is",i**2)