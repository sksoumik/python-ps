class Vars:
    def __init__(self):
        self.a = 10
        self.b = 20


var = Vars()
print(vars(var))  # {'a': 10, 'b': 20}