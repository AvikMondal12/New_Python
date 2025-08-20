# to check ositive or negtive and zero
num =float(input("Enter the of number :"))
def pos_neg(num):
    if(num==0):
        print(num ,"is a zero")

    elif(num > 0):
        print(num ,"is positive number .")
    elif(num<0):
        print(num,"This is a negtive number")
    else:
        print(num,"is a invalid number.")
pos_neg(num)