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
#Sorting using sort function
list2.sort()
#reverse using reversing function
list2.reverse()

#array slice
print(list2[:3])
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


# org_list = list(range(1,11))
# print(org_list)
# # print(type(org_list))

# org_list.append(12)
# print(org_list)

# org_list.insert(2,50)
# print(org_list)
# print(org_list)
# print(org_list[:5])
# print(org_list[-5:])
# print(org_list[1::2])

