class Film:
    genre = "Comedy"

    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year


# instantiate the Film class
obj_wows = Film("Wolf of Wall Street", 2014)
obj_ho = Film("Hang Over", 2016)

# access the class attributes
print("Wolf of Wall Street's genre is {}".format(obj_wows.__class__.genre))
print("Hang Over's genre is {}".format(obj_wows.__class__.genre))

# access the instance attributes
print(f"{obj_wows.name} released in {obj_wows.release_year}")
print(f"{obj_ho.name} released in {obj_ho.release_year}")
