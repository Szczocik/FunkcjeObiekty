import pprint
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
        self.class_teacher_list = {}
        self.object_list = []

    def add_teacher(self):

        nauczyciel = Teacher()
        nauczyciel.load(self)


        # self.first_name = input('Podaj imię: ')
        # self.name = input('Podaj nazwisko: ')
        # self.object = input('Podaj przedmiot: ')

        # while True:
        #     self.number_class = input('Podaj klasę: ')
        #     if len(self.number_class) == 0:
        #         break
        #
        #     if not self.object_list.get(self.object):
        #         self.object_list[self.object] = {'number_class':[f'{self.number_class}'],'teachers':[f'{self.first_name} {self.name}']}
        #     else:
        #         if self.number_class not in self.object_list[self.object]['number_class']:
        #             self.object_list[self.object]['number_class'].append(f'{self.number_class}')


    def show_object_list(self):
        if not self.object_list:
            print('Lista przedmiotów jest pusta')
        else:
            print(self.object_list)


    def add_student(self):
        uczen = Student()
        uczen.load(self)


        print(self.class_list)

    def show_students_list(self):
        if not self.students_list:
            print('Lista uczniów jest pusta')
        else:
            for name, value in self.object_list.items():
                for c in value['number_class']:
                    print(name, self.class_list[c]['students'], value['teachers'])



    def add_class_teacher(self):
        wychowawca = ClassTeacher
        wychowawca.load(self)

        # self.first_name = input('Podaj imię: ')
        # self.name = input('Podaj nazwisko: ')
        #
        # while True:
        #     self.number_class = input('Podaj klasę: ')
        #     if len(self.number_class) == 0:
        #         break
        #     if not self.class_teacher_list.get(f'{self.first_name} {self.name}'):
        #         self.class_teacher_list[f'{self.first_name} {self.name}'] = {'class': [self.number_class]}
        #     else:
        #         self.class_teacher_list[f'{self.first_name} {self.name}']['class'].append(self.number_class)
        #         print(self.class_teacher_list)

    def show_class_teacher_students(self):
        if not self.class_teacher_list:
            print('Lista klas jest pusta')
        else:
            for name, value in self.class_teacher_list.items():
                for c in value['class']:
                    print(f'Wychowawca: {name}, lista uczniów w klasie: ', self.class_list[c]['students'])

    def show_students_class_teacher(self):
        if not self.class_teacher_list:
            print('Lista klas jest pusta')
        else:
            pass

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

        if not school.class_list.get(self.number_class):
            school.class_list[self.number_class] = {'students':[self]}
        else:
            school.class_list[self.number_class]['students'].append(self)

    def __repr__(self):
        return f'({self.first_name} {self.name}, klasa {self.number_class})'


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
        k = f'{self.first_name} {self.name}'
        if k not in school.teachers_list:
            school.teachers_list[k] = [self]
        else:
            school.teachers_list[k].append(self)

        while True:
            number_class = input('Podaj klasę: ')
            if not number_class.strip():
                break
            self.class_list.append(number_class)

    def __repr__(self):
        return f'({self.first_name} {self.name}, klasa {self.class_list}, przedmiot {self.object})'



class ClassTeacher:
    def __init__(self):
        self.first_name = ''
        self.name = ''
        self.class_list = []

    def load(self, school):
        self.first_name = input('Podaj imię: ')
        self.name = input('Podaj nazwisko: ')

        school.object_list.append(self)
        k = f'{self.first_name} {self.name}'
        if k not in school.teachers_list:
            school.class_teacher_list[k] = [self]
        else:
            school.class_teacher_list[k].append(self)

        while True:
            number_class = input('Podaj klasę: ')
            if not number_class.strip():
                break
            self.class_list.append(number_class)

    def __repr__(self):
        return f'({self.first_name} {self.name}, klasa {self.class_list})'

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


if mode == 'nazwa':
    szkola.show_class_teacher_students()
if mode == 'wychowawca':
    pass
    # szkola.show_students_class_teacher()
if mode == 'nauczyciel':
    pass
if mode == 'uczen':
    szkola.show_students_list()



