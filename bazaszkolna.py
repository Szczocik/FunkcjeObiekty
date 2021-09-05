

PHRASE = ('nazwa klasy', 'wychowawca', 'nauczyciel', 'uczen')  # dozwolone komendy uruchomienia wejścia
USER_TYPE = ('uczen', 'nauczyciel', 'wychowawca', 'koniec')  # dozwolone komendy uruchomienia programu

class_list = []


mentor_list = []

class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.tichers_list = []
        self.studends_list = []


class Student:
    def __init__(self, name, first_name, number_class):
         self.name = name
         self.first_name = first_name
         self.number_class = number_class

    def add_student(self):
        studends_list.append(f'{name}, {surname},{number_class}')


class Teacher:
    def __init__(self, name, surname, object):
        self.name = name
        self.surname = surname
        self.object = object

         # print(uczen_1.name)
         # print(uczen_1.surname)
         # print(uczen_1.number_class)

# uczen_1 = Student('Fanek', 'Kowalski')
# uczen_1.show_student()





while True:
    command = input("Wpisz typ użytkownika: ")

    if command not in USER_TYPE:
        print("Wybierz poprawną komendę: 'uczen', 'nauczyciel', 'wychowawca', 'koniec': ")
        continue
    if command == 'koniec':
        print("Koniec programu!")
        break

    if command == 'uczen':
        name = input('Podaj imię: ')
        surname = input('Podaj nazwisko: ')
        number_class = input('Podaj numer klasy: ')
        uczen = f'{name}, {surname}, {number_class}'
        studends_list.appent(uczen)


        break
    if command == 'nauczyciel':
        teacher_name = input('Podaj imię: ')
        teacher_surname = input('Podaj nazwisko: ')
        subject = input('Przedmiot: ')
        techer_class_number = input('Podaj numer klasy: ')
        if techer_class_number == '':
            break