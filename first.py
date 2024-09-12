class Employee:
     def __init__(self,fname,lname,salary):
          self.fname = fname
          self.lname = lname
          self.salary = salary


nitin = Employee("nitin","bharadwaj",44000)
rohan = Employee("rohan","das",44000)

print(nitin.fname,rohan.fname)