
class Employee:
    # init acts like a constructor, it invokes whenever an object is created.
    def __init__(self, name, age, id, salary):
        self.name = name  # self is an instance of a class
        self.age = age
        self.id = id
        self.salary = salary


emp1 = Employee("Soumik", 24, 15111109, 50000)
emp2 = Employee("Kabir", 25, 15311109, 60000)
# emp1 and emp2 are two objects of class Employee.
print(emp1.__dict__)