"""
A pythonic way to write getter, setter and deleter in OOP. 
"""


class GetSet:
    def __init__(self):
        self.x = None

    @property
    def value(self):
        return self.x

    @value.setter
    def value(self, v):
        self.x = v

    @value.deleter
    def value(self):
        del self.x


if __name__ == "__main__":
    obj = GetSet()
    obj.value = "Sadman Kabir Soumik"  # setter is called
    get = obj.value  # getter is called
    print(obj.value)
    del obj.value  # deleter is called
    print(obj.value)  # gives error
