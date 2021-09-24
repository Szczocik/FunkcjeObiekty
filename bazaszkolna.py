
import sys

PHRASE = ('nazwa klasy', 'wychowawca', 'nauczyciel', 'uczen')  # dozwolone komendy uruchomienia wejścia
USER_TYPE = ('uczen', 'nauczyciel', 'wychowawca', 'koniec')  # dozwolone komendy uruchomienia programu


mode = sys.argv[1]


class School:
    def __init__(self):

        self.students_list = []
        self.teachers_list = {}
        self.class_list = {}
        self.class_teacher_list = {}
        self.object_list = []

    def get_group(self, symbol):
        if symbol in self.class_list:
            return self.class_list[symbol]
        self.class_list[symbol] = Group(symbol)
        return self.class_list[symbol]

    def add_teacher(self):
        nauczyciel = Teacher()
        nauczyciel.load(self)

    def add_student(self):
        uczen = Student()
        uczen.load(self)

    def add_class_teacher(self):
        wychowawca = ClassTeacher()
        wychowawca.load(self)


class Group:
    def __init__(self, symbol):
        self.symbol = symbol
        self.class_teachers = []
        self.teachers = []
        self.students = []


class Student:
    def __init__(self):
        self.first_name = ''
        self.name = ''
        self.number_class = ''

    def load(self, school):
        self.first_name = input('Podaj imię: ')
        self.name = input('Podaj nazwisko: ')
        self.number_class = input('Podaj klasę: ')

        school.students_list.append(self)
        group = school.get_group(self.number_class)
        group.students.append(self)


class Teacher:
    def __init__(self):
        self.first_name = ''
        self.name = ''
        self.object = ''
        self.class_list = []

    def load(self, school):
        self.first_name = input('Podaj imię: ')
        self.name = input('Podaj nazwisko: ')
        self.object = input('Podaj przedmiot: ')

        school.object_list.append(self)
        b = f'{self.first_name} {self.name}'
        school.teachers_list[b] = self

        while True:
            number_class = input('Podaj klasę: ')
            if not number_class.strip():
                break
            group = school.get_group(number_class)
            group.teachers.append(b)
            self.class_list.append(number_class)


class ClassTeacher:
    def __init__(self):
        self.first_name = ''
        self.name = ''
        self.class_list = []

    def load(self, school):
        self.first_name = input('Podaj imię: ')
        self.name = input('Podaj nazwisko: ')

        school.object_list.append(self)
        a = f'{self.first_name} {self.name}'
        if a not in school.class_teacher_list:
            school.class_teacher_list[a] = [self]
        else:
            school.class_teacher_list[a].append(self)

        while True:
            number_class = input('Podaj klasę: ')
            if not number_class.strip():
                break
            group = school.get_group(number_class)
            group.class_teachers.append(a)
            self.class_list.append(number_class)


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
        continue
    if command == 'nauczyciel':
        szkola.add_teacher()
    if command == 'wychowawca':
        szkola.add_class_teacher()

if mode not in szkola.class_list:
    print(f'Nie ma klasy {mode} w szkole')
else:
    print(szkola.class_list[mode].students)
    print(szkola.class_list[mode].class_teachers)

if mode == 'wychowawca':
    first_name = input('Podaj imię: ')
    name = input('Podaj nazwisko: ')
    k = f'{first_name} {name}'
    for class_teacher in szkola.class_teacher_list[k]:
        for class_name in class_teacher.class_list:
            print(szkola.class_list[class_name].students)

if mode == 'nauczyciel':
    first_name = input('Podaj imię: ')
    name = input('Podaj nazwisko: ')
    k = f'{first_name} {name}'
    for kl in szkola.teachers_list[k].class_list:
        print(szkola.class_list[kl].class_teachers)

if mode == 'uczen':
    first_name = input('Podaj imię: ')
    name = input('Podaj nazwisko: ')
    k = f'{first_name} {name}'
    for k in szkola.students_list:
        for teacher in szkola.class_list[k.number_class].teachers:
            print(f'{teacher}: {szkola.teachers_list[teacher].object}')
