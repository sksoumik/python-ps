# Parent Class
class Dog:
    def __init__(self):
        print("Dog from parent class")

    def who_is_this(self):
        print("Dog")

    def bark(self):
        print("Start Barking")


class GoldenRetriever(Dog):
    def __init__(self):
        super().__init__()
        print("Dog from child class")

    def who_is_this(self):
        print("Golden Retriever")

    def cuteness(self):
        print("Overloaded")


if __name__ == "__main__":
    golden = GoldenRetriever()
    golden.who_is_this()
    """
    As the GoldenRetriever Class extends Dog
    instances of GoldenRetriever can also use the
    instance methods of Dog Class
    """
    golden.bark()
