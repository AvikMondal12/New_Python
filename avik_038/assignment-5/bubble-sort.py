num = [7,6,5,4,3,2,1]
step=0
# Bubble sort algorithm
for i in range(len(num)):
    step+=1
    for j in range(len(num) - 1):
       
        if num[j] > num[j + 1]:
            # Swap the elements
            num[j], num[j + 1] = num[j + 1], num[j]
            
# Print the sorted list
    print("Sorted list:", num)
    
print(step)