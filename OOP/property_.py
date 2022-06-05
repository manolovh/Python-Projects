class Movie:

    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if 1 <= new_rating <= 5:
            self._rating = new_rating
        else:
            print("Please enter a valid rating")


movie = Movie('blue', 9.5)

print(movie.rating)

movie.rating = 1.22

print(movie.rating)
