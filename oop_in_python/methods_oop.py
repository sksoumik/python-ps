class Film:
    # instane attributes
    def __init__(self, movie_name, release_year):
        self.movie_name = movie_name
        self.release_year = release_year

    # instance method
    def cast(self, actor):
        return "{} acted in {}".format(actor, self.movie_name)

    # instance method
    def director(self, director):
        return "{} directed {}".format(director, self.movie_name)


if __name__ == "__main__":
    # instantiate the objects
    movie_obj = Film("Inception", 2012)

    # call instance method
    print(movie_obj.director("Cristopher Nolan"))
