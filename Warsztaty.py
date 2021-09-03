# Warsztaty
import self as self

ALLOWED_COMMANDS = ('add', 'books', 'delete','stop')


class Biblioteka:
    '''Klasa reprezentująca bibliotekę,
    która grupuje książki i użytkówników'''
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
        self.users = []
    def show_books(self):
        if not self.books:
            print('Pusta baza książek!')
        else:
            print(self.books)

    def add_book(self):
        title = input('Tytuł: ')
        autor = input('Autor: ')
        id = self.set_book_id()
        book = Book(id=id, title=title, author=autor)
        self.books.append(book)
        print(f'Książka {book} dodana do bazy!')

    def delete_book(self):
        id = int(input('Podaj ID książki do usunięcia: '))
        for index, book in enumerate(self.books):
            if id == book.id:
                print(f'USUWAM! {book}')

    def set_book_id(self):
        if not self.books:
            return 1
        return len(self.books) + 1



class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.status = 'available'
        self.user = None
        self.return_date = None

    def __str__(self):
        return f'({self.id}) {self.title} - {self.author}'

    def __repr__(self):
        return f'({self.id}) {self.title} - {self.author}'

class User:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.books = []
        self.first_name = first_name
        self.last_name = last_name





class Administrator:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password


bib = Biblioteka(address='Warszawa', name='Moja Biblioteka')


while True:
    command = input('Podaj komendę: ')
    if command not in ALLOWED_COMMANDS:
        print(f'Niepoprawna komenda! Dostępne komendy: {ALLOWED_COMMANDS}')
        continue
    if command == 'stop':
        break
    if command == 'add':
        bib.add_book()
    if command == 'delete':
        bib.delete_book()
    if command == 'books':
        bib.show_books()
#
#
#
#
#
# # number = 1
#
# # if isinstance(bib, Biblioteka)
# # pass