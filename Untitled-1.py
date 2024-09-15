class Employee:
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    # New code
    def emp_details(self):
        print(f"Employee role no. is {self.fname} {self.lname} and salary is {self.salary}.")

        


# New code
def student_details(role,name,age):
    print(f"Student role no. is {role}, name is {name} and age is {age}.")
     


nitin = Employee("nitin","bharadwaj",44000)
rohan = Employee("rohan","das",44000)

print("1. ", nitin.fname,rohan.fname)


# New code
"""
Display student details
"""
# print("2. student_details: ", student_details.role)

"""
Start- Exception Handling
"""
a = "abc" # pass
try: # pass
    print("try a1: ", a) # pass
    print("try 2. student_details: ", student_details.role) 
    print("try a2: ", a) # pass
except Exception as nitin: # fail
    print("except nitin: ", nitin)
    a='xyz' # fail
    print("except a3: ", a) # fail
else: # pass
    print("else block of try!!!!!!!!!!!!!!") # pass
finally: # pass
    print("Finally a4: ", a) # pass 

"""
End- Exception Handling
"""


print("3. student_details DIR: ", dir(student_details)) # pass