class Employee:
     increment = 1.5  # Class variable
     no_of_employees = 0
     
     def __init__(self,fname, lname, salary):
          self.fname = fname
          self.lname = lname
          self.salary = salary
          Employee.no_of_employees +=1

     def increase(self):
          salary = int(salary * Employee.increment)
     
     @classmethod
     def change_increment(cls,amount):
          cls.increment=amount

     @classmethod 
     def from_str(cls,emp_string):
          fname,lname,salary = emp_string.split("-")
          return cls(fname,lname,salary)

nitin = Employee("Nitin","Bharadwaj",66000)
rohit = Employee.from_str("rohit-dubey-33000")
rohan = Employee("rohan","das",66000)


print(rohit.salary)
Employee


#print(Employee.no_of_employees)
#nitin = Employee("nitin", "bharadwaj", 44000)
#print(Employee.no_of_employees)
#rohan = Employee("rohan", "das", 44000)
#print(Employee.no_of_employees)

#print(nitin.__dict__)
#itin.increment = 9
#print(nitin.__dict__)

#print(nitin.salary)
#nitin.increase()  

#print(Employee.__dict__)