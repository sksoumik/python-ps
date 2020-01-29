class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def do_something(self):
        print("Hi from {}".format(str(self)))

    def __str__(self):
        return self.name + ", " + self.email


if __name__ == "__main__":
    users = [
        User("Soumik", "sadmanks@gmail.com"),
        User("Kabir", "sksoumik.ai@gmail.com")
    ]

    for user in users:
        user.do_something()
