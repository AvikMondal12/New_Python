# class Student():
#    cogName ="Brainware University"
#    def __init__(self,fullname,role):   # __init__ means that we create a constractor
#     self.name=fullname     # self is the first argument of the constractor that compalsury
    
#     self.role=role
  
  
# s1 = Student("avik",38)  # s1 is an object that you also called it as variable where store our class
# print(s1.name,s1.role,s1.cogName)

# s1 = Student("suman",39)       # S1=self 
# print(s1.name,s1.role,s1.cogName)
# s1 = Student("kuntal",37)
# print(s1.name,s1.role,s1.cogName)



# class Student():
#    cogName ="Brainware University"
#    name = "suman"  # Class attribute
   
#    def __init__(self,fullname,role): 
#     self.name=fullname #It is called object attribute             
#     # When we have 2 same name atrribut then always it take first as the object attribute
    
#     self.role=role
  
  
# s1 = Student("avik",38)  
# print(s1.name,s1.role,s1.cogName)


# class Student:
  
#   def __init__(self,fullname,marks):
#     self.name=fullname
#     self.marks=marks
    
#   def hello(self):
#     print("Name =  ",self.name)
      
#   def mark(self):
#     print("Marks = ",self.marks)
    
# s1 = Student("Avik",67)
# s1.hello()

# s1.mark()
    
    
    
# class Student:
#   Clg_name = "Brainware University"
#   batch =2025
#   def __init__(self,name ,roll,phone,address):
#     self.name=name 
#     self.roll=roll
#     self.phone=phone
#     self.address=address
    
    
#   #This function is for Name pof the student 
#   def std_name(self):
#     print("Name is :",self.name)
    
#   # This function is for Roll of the student 
#   def std_roll(self):
#     print("Roll is : ",self.roll)
  
#   #This function is for Phone number of the student 
#   def std_phone(self):
#     print("Phone no. is : ",self.phone)
  
#   #This function is for Address of the student 
#   def std_addr(self):
#     print("Address is :",self.address)
    
# s1 = Student("Avik",38,9832711018,"Bardhaman")
# print(s1.Clg_name,s1.batch)
# s1.std_name()

# s1.std_roll()
# s1.std_phone()
# s1.std_addr()


# s1 = Student("Kuntal",37,98376718,"Hawrah")
# print("\n",s1.Clg_name,s1.batch)
# s1.std_name()

# s1.std_roll()
# s1.std_phone()
# s1.std_addr()


# class Student:
  
#   def __init__(self,roll,name):
#     self.name= name 
#     self.roll=roll
    
# s1 =Student(37,"Kuntal")
# print(s1.name,s1.roll)

# s1 =Student(38,"Avik")
# print(s1.name,s1.roll)



# class Student:
#   def __init__(self,name,math,phy,eng):
#     self.math=math
#     self.name=name
#     self.eng=eng
#     self.phy=phy
    
# s1 = Student("Avik",76,6,76)
# print(s1.name)
# avg = (s1.math+s1.phy+s1.eng)/3
# print(avg)

# s1 = Student("Kuntal",76,87,98)
# print(s1.name)
# avg = (s1.math+s1.phy+s1.eng)/3
# print(avg)


# s1 = Student("Manish",98,88,99)
# print(s1.name)
# avg = (s1.math+s1.phy+s1.eng)/3
# print(avg)

# s1 = Student("Suman",77,46,66)
# print(s1.name)
# avg = (s1.math+s1.phy+s1.eng)/3
# print(avg)

# class student :
#   # @staticmethod
#   def hello():
#     print("HEllo World")

# s1 = student()
# s1.hello()


#private class

class Student :
  __name = "Avik"
  print(__name)
  
s1 = Student
print(s1.__name)