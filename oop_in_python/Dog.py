"""

"""
class Dog:
    species = "mammal"

    # Initializer / Instance Attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old.".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


"""********************************* RussellTerrier   *********************************"""
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {} speed".format(self.name, speed)



"""***************************    BullDog   *****************************************"""
class BullDog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


"""********************************************************************"""
lalo  = Dog("Lalo", 5)
trump = Dog("Trump", 21)
print("{} is {} and {} is {} ".format(lalo.name, lalo.age, trump.name, trump.age))

# IS lalo a mammal?
if lalo.species == "mammal":
    print("{} is a {}".format(lalo.name, lalo.species))

lalo_desc = lalo.description()
print(lalo_desc)

lalo_sound = lalo.speak("Bhog bhog gheu gheu")
print(lalo_sound)

trump_sound = trump.speak("Let's make America great again.")
print(trump_sound)

"""********************************************************************"""

devid = BullDog("Devid", 10)
print(devid.description())
print(devid.run(100)+ " km/h")

