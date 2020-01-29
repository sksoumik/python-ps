class GetSet:
    def __init__(self, x):
        self.x = x

    def getter(self):
        return self.x

    def setter(self, value):
        self.x = value

    def deleter(self):
        del self.x


if __name__ == "__main__":
    obj = GetSet(10)
    print(obj.getter())
