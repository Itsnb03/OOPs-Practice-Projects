class Employee:
     def __init__(self,fname,lname,salary):                     
          self.fname = fname
          self.lname = lname
          self.salary = salary

class Std:
     

    def __init__(self,name):
     self.name=name

    def __init__(self,classno):
     self.jobtitle=classno

    def __init__(self,college): 
     self.college=college

    def __init__(self,rollno):
     self.rollno=rollno    
        
college = Std("rahul","manager",504,"mumbai",04)



print(Std.name)



nitin = Employee("nitin","bharadwaj",44000)
rohan = Employee("rohan","das",44000)

type(nitin)








"""code review
Q1.pre-define keywords in this program = 
ans. class,def,__init__,self,print

Q2.what is class ?
ans. class works as template or blueprint for the program

Q3.what is def?
ans. def is use for defining function

Q4.difference between function and method ?
ans. A function doesn't need any object and is independent, while the method is a function, which is linked with any object. We can directly call the function with its name, while the method is called by the object's name. Function is used to pass or return the data, while the method operates the data in a class.

Q5. What is __init__() method?
ans. spacial method of a class known as constuctor

Q6. Is self pre-define keywords?
ans. No, It is an default first argument

"""