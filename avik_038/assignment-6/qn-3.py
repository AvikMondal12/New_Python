#Define a function using keyword argument to print employee details
def emp_dlt(**kwargs):
    for key , value in kwargs.items():
        print(f"{key} : {value}")

emp_dlt(Name = "Avik", age = 21, role = "IT")