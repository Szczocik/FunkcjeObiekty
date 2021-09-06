

PHRASE = ('nazwa klasy', 'wychowawca', 'nauczyciel', 'uczen')  # dozwolone komendy uruchomienia wejścia
USER_TYPE = ('uczen', 'nauczyciel', 'wychowawca', 'koniec')  # dozwolone komendy uruchomienia programu






class School:
    def __init__(self):
        self.students_list = []
        self.tichers_list = []
        self.class_list = []
        self.mentor_list = []


    def add_student(self):
        self.first_name = input('Podaj imię: ')
        self.name = input('Podaj nazwisko: ')
        self.number_class = input('Podaj klasę: ')
        uczen = Student(first_name=self.first_name, name=self.name, number_class=self.number_class)
        self.students_list.append(uczen)




    def show_students_list(self):
        if not self.students_list:
            print('Lista uczniów jest pusta')
        else:
            print(self.students_list)




class Student:
    def __init__(self, first_name, name, number_class):
        self.first_name = first_name
        self.name = name
        self.number_class = number_class

    def __repr__(self):
        return f'({self.first_name} {self.name}, klasa {self.number_class})'





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

szkola = School()



while True:
    command = input("Wpisz typ użytkownika: ")
    if command not in USER_TYPE:
        print(f"Wybierz poprawną komendę: {USER_TYPE}")
        continue
    if command == 'koniec':
        print("Koniec programu!")
        break
    if command == 'uczen':
        szkola.add_student()
        szkola.show_students_list()
        continue
    else:
        break



        # if command == 'nauczyciel':
        #     teacher_name = input('Podaj imię: ')
        #     teacher_surname = input('Podaj nazwisko: ')
        #     subject = input('Przedmiot: ')
        #     techer_class_number = input('Podaj numer klasy: ')
        # if techer_class_number == '':
        #     break