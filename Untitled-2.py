class Employee:
    # New code
    def emp_details():
        print(f"Employee is Nitin Bhardwaj and salary is 50k.")
        return f"It is return value of emp_details."

# New code
def student_details():
    print("-------------------------")
    print(f"Student role no. is 101, name is Nitin and age is 18.")
    print("-------------------------")
    return f"It is return value."

# New code
"""
Display student details
"""

# function call
student_details()

# New code
"""
Display employee details
"""
employee_object_one = Employee

# function call from class
employee_object_one.emp_details()