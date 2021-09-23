
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

        print(self.class_list)

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

        # if not school.class_list.get(self.number_class):
        #     school.class_list[self.number_class] = {'students': [self]}
        # else:
        #     print(school.class_list[self.number_class])
        # school.class_list[self.number_class].students.append(self)

        print(school.students_list)

    def __repr__(self):
        return f'({self.first_name} {self.name})'


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
        if b not in school.teachers_list:
            school.teachers_list[b] = [self]
        else:
            school.teachers_list[b].append(self)

        while True:
            number_class = input('Podaj klasę: ')
            if not number_class.strip():
                break
            group = school.get_group(number_class)
            group.teachers.append(b)
            self.class_list.append(number_class)
        print(school.teachers_list)

    def show(self, school):
        for symbol in self.class_list:
            group = school.get_group(symbol)
            for student in group.students:
                print(student)

    # def __repr__(self):
    #     return f'klasy {self.class_list}, przedmiot {self.object})'


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
        print(school.class_teacher_list)

    def show(self, school):
        for symbol in self.class_list:
            group = school.get_group(symbol)
            for student in group.students:
                print(student)


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
            print(class_name)
            print(szkola.class_list[class_name].students)

if mode == 'nauczyciel':
    first_name = input('Podaj imię: ')
    name = input('Podaj nazwisko: ')
    k = f'{first_name} {name}'
    for klasa in szkola.teachers_list[k].class_list:
        szkola.class_list[klasa].class_teachers

    print(szkola.teachers_list[k].class_list)
        # for class_name in teacher.class_list:
        #     print(class_name)
        # for class_name in teacher_list.class_list:
        #     print(class_name)
        #     print(szkola.class_list[class_name].teacher)
if mode == 'uczen':
    first_name = input('Podaj imię: ')
    name = input('Podaj nazwisko: ')
    k = f'{first_name} {name}'
    for k in szkola.class_list.keys():
        print(k)

        # for class_name in students.class_list:
        #     print(class_name)
