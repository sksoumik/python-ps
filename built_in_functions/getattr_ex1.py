class Getattr:
    def __init__(self):
        self.name = 'Java'
        self.version = 8


obj = Getattr()
print("The version of the {} is {}".format(getattr(obj, 'name'),
                                           getattr(obj, 'version')))
