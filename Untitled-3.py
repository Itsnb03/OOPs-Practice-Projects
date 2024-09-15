class Employee:
    def __init__(pqr, via_class_name):
        pqr.xyz = via_class_name
     
    def emp_detail(pqr, via_method_name):
        print(f"via_class_name Employee is {pqr.xyz} Bhardwaj and salary is 50k.")
        print(f"via_method_name Employee is {via_method_name} Bhardwaj and salary is 50k.")
     
emp_obj_one = Employee("Nitish")
emp_obj_one.emp_detail("Nitin")

emp_obj_two = Employee("abc")
emp_obj_two.emp_detail("xyz")