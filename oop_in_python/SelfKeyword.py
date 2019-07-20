class SelfKeyword:
    variable_1 = "This is a class variable"
    variable_2 = 100  # this is also a class variable

    def __init__(self, param_1, param_2):
        self.variable_1 = param_1
        self.variable_2 = param_2

# Creating instance of SelfKeyword class
obj1 = SelfKeyword("Some thing", 18)
obj2 = SelfKeyword(10,20)

print(obj1.variable_1)
print(obj2.variable_1)
