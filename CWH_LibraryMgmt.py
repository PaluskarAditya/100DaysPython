class Library:
    def append(self, name):
        self.books.append(name)

    def __init__(self):
        self.books = []
        self.no_of_books = 0
        
    def all_books(self):
        for book in self.books:
            print(book)
        print(f"available books: {self.no_of_books}")        
        
    def add_book(self, book_name):
        self.append(book_name)
        self.no_of_books += 1          