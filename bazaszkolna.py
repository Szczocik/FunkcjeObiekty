import sys

PHRASE = ('nazwa klasy', 'wychowawca', 'nauczyciel', 'uczen')  # dozwolone komendy uruchomienia wejścia
USER_TYPE = ('uczen', 'nauczyciel', 'wychowawca', 'koniec')  # dozwolone komendy uruchomienia programu
# mode = PHRASE


mode = sys.argv[1]

class School:
    def __init__(self):

        self.students_list = []
        self.teachers_list = {}
        self.class_list = {}
        self.mentor_list = []
        self.class_teacher_list = {}
        self.object_list = {}

    def add_teacher(self):
        self.first_name = input('Podaj imię: ')
        self.name = input('Podaj nazwisko: ')
        self.object = input('Podaj przedmiot: ')

        while True:
            self.number_class = input('Podaj klasę: ')
            if len(self.number_class) == 0:
                break

            if not self.object_list.get(self.object):
                self.object_list[self.object] = {'number_class':[f'{self.number_class}'],'teachers':[f'{self.first_name} {self.name}']}
            else:
                if self.number_class not in self.object_list[self.object]['number_class']:
                    self.object_list[self.object]['number_class'].append(f'{self.number_class}')


    def show_object_list(self):
        if not self.object_list:
            print('Lista przedmiotów jest pusta')
        else:
            print(self.object_list)


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
        print(self.class_list)

    def show_students_list(self):
        if not self.students_list:
            print('Lista uczniów jest pusta')
        else:
            print(self.students_list)
            print(self.class_list)

    def add_class_teacher(self):
        self.first_name = input('Podaj imię: ')
        self.name = input('Podaj nazwisko: ')

        while True:
            self.number_class = input('Podaj klasę: ')
            if len(self.number_class) == 0:
                break
            if not self.class_teacher_list.get(f'{self.first_name} {self.name}'):
                self.class_teacher_list[f'{self.first_name} {self.name}'] = {'class': [self.number_class]}
            else:
                self.class_teacher_list[f'{self.first_name} {self.name}']['class'].append(self.number_class)
                print(self.class_teacher_list)

    def show_class_teacher_students(self):
        if not self.class_teacher_list:
            print('Lista klas jest pusta')
        else:
            for name, value in self.class_teacher_list.items():
                for c in value['class']:
                    print(name, self.class_list[c]['students'])

    def show_students_class_teacher(self):
        if not self.class_teacher_list:
            print('Lista klas jest pusta')
        else:
            for name, value in self.class_teacher_list.items():
                for c in value['class']:
                    print(name, self.class_list[c]['students'])


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



    def __repr__(self):
        return f'({self.first_name} {self.name}, przedmiot {self.object})'

class ClassTeacher:
    def __init__(self, first_name, name, number_class):
        self.first_name = first_name
        self.name = name
        self.number_class = number_class


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
        szkola.show_object_list()
    if command == 'wychowawca':
        szkola.add_class_teacher()
        # szkola.show_class_teacher_students()

if mode == 'nazwa klasy':
    szkola.show_students_class_teacher()
if mode == 'wychowawca':
    szkola.show_students_class_teacher()
if mode == 'nauczyciel':
    pass
if mode == 'uczen':
    pass


