class Library:
    def __init__(self,book,no_of_books):
        self._book = book
        self._no_of_books = no_of_books

    @property
    def showBooks(self):
        print(f"The books are {self._book},{self._no_of_books}")

    @showBooks.setter
    def showBooks(self, new_book):
        self._book.append(new_book)
        
    def Check(self):
        if self._no_of_books == len(self._book):
            print("The count and number in the list are equal")
        else:
            print("The count is not equal")


    

Lib1 = Library(["A","B","C"], 4)
Lib1.showBooks = "d"
Lib1.showBooks

Lib1.Check()
