class Getattr:
    def __init__(self, name, version):
        self.name = name
        self.version = version


obj = Getattr('python', 3.6)
print(obj.name, obj.version)  # convensional way
print(getattr(obj, 'name'), getattr(obj, 'version'))  # Using getattr
