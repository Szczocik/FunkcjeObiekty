

PHRASE = ('nazwa klasy', 'wychowawca', 'nauczyciel', 'uczen')  # dozwolone komendy uruchomienia wejścia
USER_TYPE = ('uczen', 'nauczyciel', 'wychowawca', 'koniec')  # dozwolone komendy uruchomienia programu






class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.tichers_list = []
        self.students_list = []
        self.class_list = []
        self.mentor_list = []

    def add_student(self):
        uczen = (f'{self.name}, {self.first_name}')
        self.student_list.append(uczen)
        print(self.student_list)


class Student:
    def __init__(self, name, first_name, number_class):
         self.name = input(name)
         self.first_name = input(first_name)
         self.number_class = input(number_class)




class Teacher:
    def __init__(self, name, first_name, object):
        self.name = name
        self.first_name = first_name
        self.object = object

         # print(uczen_1.name)
         # print(uczen_1.surname)
         # print(uczen_1.number_class)

# uczen_1 = Student('Fanek', 'Kowalski')
# uczen_1.show_student()

szkola = School(name="Szkoła", address="Warszawa")




while True:
    command = input("Wpisz typ użytkownika: ")
    if command not in USER_TYPE:
        print(f"Wybierz poprawną komendę: {USER_TYPE}")
        continue
    if command == 'koniec':
        print("Koniec programu!")
        break
    else:
        name = input('Podaj imię: ')
        first_name = input('Podaj nazwisko: ')
        if command == 'uczen':
            student.add_student()



        break
        if command == 'nauczyciel':
            teacher_name = input('Podaj imię: ')
            teacher_surname = input('Podaj nazwisko: ')
            subject = input('Przedmiot: ')
            techer_class_number = input('Podaj numer klasy: ')
        if techer_class_number == '':
            break