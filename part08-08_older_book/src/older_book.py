# DO NOT CHANGE CLASS Book!
# Write your solution after the class!

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

# -----------------------------
# Write your solution here
# -----------------------------
def older_book(book1: Book, book2: Book):
    year1 = book1.year
    year2 = book2.year
    if year1 > year2:
        print(f"{book2.name} is older, it was published in {year2}")
    elif year1 < year2:
        print(f"{book1.name} is older, it was published in {year1}")
    else:
        print(f"{book1.name} and {book2.name} were published in {year1}")

if __name__ == "__main__":
    python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
    everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)
    norma = Book("Norma", "Sofi Oksanen", "crime", 2015)

    older_book(python, everest)
    older_book(python, norma)