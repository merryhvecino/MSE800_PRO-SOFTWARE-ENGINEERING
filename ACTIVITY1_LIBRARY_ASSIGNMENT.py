class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
        
    def show_books(self):
        print('/nBooks in the Library:')
        for book in self.books:
            print(book)
            
lib = Library()
for i in range(3):
    book = input(f'Enter the Book Name{i+1}:' )
    lib.add_book(book)

lib.show_books()