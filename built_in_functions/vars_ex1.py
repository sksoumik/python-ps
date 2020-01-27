"""
vars() method takes only one parameter and that too is optional. It takes 
an object as a parameter which may be can a module,
a class, an instance, or any object having __dict__ attribute.
"""


class VarSample:
    def __init__(self, name='soumik', dept='cse'):
        self.name = name
        self.dept = dept


var_sample = VarSample()
print(vars(var_sample))

# {'name': 'soumik', 'dept': 'cse'}
