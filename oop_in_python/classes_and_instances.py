class Employee:
    def __init__(self, first_name, last_name, payment):
        self.first_name = first_name
        self.last_name = last_name
        self.payment = payment
        self.email = first_name.lower() + '.' + last_name.lower() + '@email.com'

    def full_name(self):
        print(self.first_name + ' ' + self.last_name)

    def employee_info(self):
        print("Name:" + self.first_name + ' ' + self.last_name +
              "\nEmail: " + self.email +
              "\nPayment: " + str(self.payment))


emp1 = Employee('Sadman', 'Soumik', 50000)
emp2 = Employee('Tamim', 'Iqbal', 60000)
print(emp1.email)
emp1.full_name()
print()
print(emp2.email)
emp2.full_name()
print("\nEmployee information: ")
emp2.employee_info()
print()
# Calling by class name
Employee.employee_info(emp1)
