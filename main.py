class Employee:
     increment = 1.5  # Class variable
     no_of_employees = 0
     
     def __init__(self, fname, lname, salary):
          self.fname = fname
          self.lname = lname
          self.salary = salary
          Employee.no_of_employees +=1

     def increase(self):
          self.salary = int(self.salary * Employee.increment)
print(Employee.no_of_employees)
nitin = Employee("nitin", "bharadwaj", 44000)
print(Employee.no_of_employees)
rohan = Employee("rohan", "das", 44000)
print(Employee.no_of_employees)



#print(nitin.__dict__)
#itin.increment = 9
#print(nitin.__dict__)

#print(nitin.salary)
#nitin.increase()  
#print(nitin.salary)  

#print(Employee.__dict__)