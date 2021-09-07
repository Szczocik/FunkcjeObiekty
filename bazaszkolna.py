

PHRASE = ('nazwa klasy', 'wychowawca', 'nauczyciel', 'uczen')  # dozwolone komendy uruchomienia wejścia
USER_TYPE = ('uczen', 'nauczyciel', 'wychowawca', 'koniec')  # dozwolone komendy uruchomienia programu






class School:
    def __init__(self):

        self.students_list = []
        self.teachers_list = []
        self.class_list = {}
        self.mentor_list = []
        self.teacher_class = []

    def add_teacher(self):
        self.first_name = input('Podaj imię: ')
        self.name = input('Podaj nazwisko: ')
        self.object = input('Podaj przedmiot: ')
        self.teacher_number_class = input('Podaj klasę: ')

        nauczyciel = Teacher(first_name=self.first_name, name=self.name, object=self.object,)
        self.teachers_list.append(nauczyciel)

        # while self.teacher_number_class != '':
        #     self.teacher_class.append(self.teacher_number_class)
        #
        # else:
        #     print(self.teacher_number_class)


    def show_teachers_list(self):
        if not self.teachers_list:
            print('Lista nauczycieli jest pusta')
        else:
            print(self.teachers_list)


    def add_student(self):
        self.first_name = input('Podaj imię: ')
        self.name = input('Podaj nazwisko: ')
        self.number_class = input('Podaj klasę: ')
        uczen = Student(first_name=self.first_name, name=self.name, number_class=self.number_class)
        self.students_list.append(uczen)
        if not self.class_list.get(self.number_class):
            self.class_list[self.number_class] = {'students':[f'{self.first_name} {self.name}']}
        else:
            self.class_list[self.number_class]['students'].append(f'{self.first_name} {self.name}')

    def show_students_list(self):
        if not self.students_list:
            print('Lista uczniów jest pusta')
        else:
            print(self.students_list)
            print(self.class_list)

class Student:
    def __init__(self, first_name, name, number_class):
        self.first_name = first_name
        self.name = name
        self.number_class = number_class

    def __repr__(self):
        return f'({self.first_name} {self.name}, klasa {self.number_class})'


class Teacher:
    def __init__(self, first_name, name, object):
        self.first_name = first_name
        self.name = name
        self.object = object
        # self.teacher_number_class = teacher_number_class


    def __repr__(self):
        return f'({self.first_name} {self.name}, przedmiot {self.object})'

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
    if command == 'nauczyciel':
        szkola.add_teacher()
        szkola.show_teachers_list()
    else:
        break

