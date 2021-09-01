

PHRASE = ('nazwa klasy', 'wychowawca', 'nauczyciel', 'uczen')  # dozwolone komendy uruchomienia wejścia
USER_TYPE = ('uczen', 'nauczyciel', 'wychowawca', 'koniec')  # dozwolone komendy uruchomienia programu

class_list = []
studends_list = []
tichers_list = []
mentor_list = []



class Student:
     def __init__(self, name, surname, number_class):
         self.name = name
         self.surname = surname
         self.number_class = number_class

     def show_student(self):
         uczen = (f'{name} {surname}, {number_class}')
         studends_list += uczen
         print(studends_list)

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
        uczen = Student(name, surname, number_class)
        studends_list += uczen

        print(studends_list)
        break