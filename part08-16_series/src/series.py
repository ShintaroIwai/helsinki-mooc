# Write your solution here:
class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.list = []

    def rate(self, rating: int):
        self.list.append(rating)
    
    def count_ratings(self):
        return len(self.list)
    
    def average_rating(self):
        count = self.count_ratings()
        if count != 0:
            return sum(self.list) / self.count_ratings()
    
    def __str__(self):
        self.ratings = self.count_ratings()
        self.average = self.average_rating()
        genre_string = ", ".join(self.genres)
        if self.ratings > 0:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\n{self.ratings} ratings, average {self.average:.1f} points"
        else:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genre_string}\nno ratings"

def minimum_grade(rating: float, series_list: list):
    eligible = []
    for series in series_list:
        if series.average_rating() >= rating:
            eligible.append(series)
    return eligible

def includes_genre(genre: str, series_list: list):
    eligible = []
    for series in series_list:
        if genre in series.genres:
            eligible.append(series)
    return eligible

if __name__ == "__main__":
    # dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    # # dexter.rate(4)
    # # dexter.rate(5)
    # # dexter.rate(5)
    # # dexter.rate(3)
    # # dexter.rate(0)
    # # print(dexter)

    # s = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    # s.rate(5)
    # s.rate(3)
    # s.rate(2)
    # print(s)

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)