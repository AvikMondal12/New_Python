#index  0,1,2,3,4,5,6,7,8,9
list = [1,2,3,4,5,6,7,8,9,10]
print(list)
#Append operation to add 12
list.append(12)
#insert operation in 
list.insert(10,11)
print(list)

del list[0] # delete elements from index 0 
print(list)


list[0]=25  # update operation
print(list)

list2 = [3,2,4,7,1]
list2.sort()
list2.reverse()
print(list2[1:3])
print(list2)

# Generate squares of even numbers from 1 to 10
list_even_no =[]
squares_of_even = []
print("Even Number of the list is :",end=" ")
for i in range(1,11):
  if(i%2==0):
    
    list_even_no.append(i)
    squares_of_even.append(i**2)    
print(list_even_no)
print("Squre of Even no. of the list: ",end=" ")
print(squares_of_even)
