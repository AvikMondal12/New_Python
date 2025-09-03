# selection sort using python 
data = []
length = int (input("Enter the list range :"))
for x in range(length):
    value = int(input("Enter the value :"))
    data.append(value)
print(data)

steps = 0

n = len(data)
for i in range(n):
    steps+=1
    min_index = i
        # Find the index of the minimum element in the remaining unsorted part
    for j in range(i + 1, n):
        if data[j] < data[min_index]:
            min_index = j
        # Swap the found minimum element with the first unsorted element
    data[i], data[min_index] = data[min_index], data[i]

# Example usage


print("Sorted array:", data)
print(steps)