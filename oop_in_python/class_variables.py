"""
Class variables are the variables that shares among all class instances
"""


class Employee:
    number_of_employee = 0
    raise_amount = 1.04  # raise amount by 4% from the previous value

    def __init__(self, first_name, last_name, payment):
        self.first_name = first_name
        self.last_name = last_name
        self.payment = payment
        self.email = first_name.lower() + '.' + last_name.lower() + '@email.com'
        Employee.number_of_employee += 1

    def apply_raise(self):
        self.payment = int(self.payment * self.raise_amount)

    def full_name(self):
        print(self.first_name + ' ' + self.last_name)

    def employee_info(self):
        print("Name:" + self.first_name + ' ' + self.last_name +
              "\nEmail: " + self.email +
              "\nPayment: " + str(self.payment))


emp1 = Employee('Sadman', 'Soumik', 50000)
emp2 = Employee('Tamim', 'Iqbal', 60000)

print(emp1.payment)
emp1.apply_raise()
print(emp1.payment)
print("Employee information of", emp1.last_name)
emp1.employee_info()
print(emp1.__dict__) # no variable named raise_amount can be found here cause emp1 is instance variable
print(Employee.__dict__) # raise_amount exists here

emp1.raise_amount = 1.10
emp1.apply_raise()
print(emp1.payment)  # only change the raise amount for emp1 not for all

# if we want to change it for all
Employee.raise_amount = 1.20
emp2.apply_raise()
print(emp2.payment) # increases by 20%

print(Employee.number_of_employee)