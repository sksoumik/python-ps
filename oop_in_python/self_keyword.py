"""
Self keyword
But before talking about the self keyword (which is actually not a python keyword
or any special literal), first, let’s recall what are class variables and instance
variables. Class variables are variables that are being shared with all instances
(objects) which were created using that particular class. So when accessed a class
variable from any instance, the value will be the same. Instance variables, on the
other hand, are variables which all instances keep for themselves (i.e a particular
object owns its instance variables).
So typically values of instance variables differ from instance to instance.
"""


class SomeClass:
    variable_1 = "This is a class variable"
    variable_2 = 100  # this is also a class variable.

    def __init__(self, param1, param2):
        self.instance_var1 = param1
        # instance_var1 is a instance variable
        self.instance_var2 = param2
        # instance_var2 is a instance variable
