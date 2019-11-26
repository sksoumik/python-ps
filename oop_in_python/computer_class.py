class Computer:
    name = "Tanisha"
    age = 14

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print("Name is {} and Age is {}".format(self.name, self.age))


info_1 = Computer("Soumik", 20)

print(info_1.name)
print(info_1.age)

info_2 = Computer("Kabir", 25)
info_2.print()

print(Computer.name)
print(Computer.age)
