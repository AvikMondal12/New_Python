num = int(input("Enter the value of  the number :"))

brk = int(input("Enter the break number :"))

skip = int(input("Enter the value of skip number :"))

for i in range(1,num+1):
    # print(i)

    if(i == brk):
        break

    elif(i==skip):
        continue
    elif(i==3):
        pass
    print(i)