#  plik warsztatowy Funkcje Obiekty PEP

# Funkcje to nazwane i odizolowane fragmenty kodu, które opcjonalnie mogą zwracać
# wartość: funkcje definiuje się przez jej nazwę, parametry i ciało (kod właśiciwy funkcji).

# Składnia:
# def nazwa_funkcji(parametr1, parametr2, parametr3, ... ,parametrn): #dwukropek na końcu
# 	kod do wykonania linia 1 #zwróć uwagę na wcięcie
# 	kod do wykonania linia 1
#  	kod do wykonania linia 1


# Funkcje

def show_separator(number):
    print("#"*number)

show_separator(50)
number_1 = float(input('Liczba 1: '))
number_2 = float(input('Liczba 2: '))
show_separator(20)
number_sum = number_1 + number_2
print(f'Suma liczb {number_1} i {number_2}')
show_separator(10)

def sum_numbers(number1, number2):
    result = number1 + number2
    return result
result = sum_numbers(2, 3)
print("Result:", result)

def sum_numbers(number1, number2):
    result = number1 + number2
    diff = number1 - number2
    return (result, diff)  # przy 2 działaniach możemy otrzymać Tuplę

result_sum, result_diff = sum_numbers(2, 3)  # możemy odrazu przyporządkować Tuplę
print("Result:", result_sum, result_diff)

def sort_numbers(a, b, c):  # w nawiasie argumenty pozycyjne
    temp = [a, b, c]
    return temp

sorted_numbers = sort_numbers(2, 3, 1)
print(sorted_numbers)

def sort_numbers(a, b, c):  # w nawiasie argumenty pozycyjne
    temp = [a, b, c]
    return sorted_temp

sorted_numbers = sort_numbers(2, 3, 1)
print(sorted_numbers)


sorted_numbers = sort_numbers(2, 3, c=1, d=3)  # argumenty pozycyjne muszą być przed przypisanymi (c=1)
print(sorted_numbers)

def sort_numbers(a, b, c=1, d=3):  # w nawiasie argumenty pozycyjne
    print("c", c)
    print("d", d)
    temp = [a, b, c, d]  # lista
    return sorted(temp)  # zwraca sortowanie listy

sorted_numbers = sort_numbers(2, 3, d=1, c=5)  # nie ma znaczenia kolejność argumentów przypisanych (c,d)
print(sorted_numbers)

def sort_numbers_other(*args): # *args określa dowolną liczbę argumentów
    #print(args)  # to jest Tupla
    temp = list(args)  # zwraca listę argumentów posortowanych [1, 2, 3, 4, 5, 6, 7]
    return  sorted(temp)

resurt = sort_numbers_other(1, 4, 5, 6, 7, 2, 3)  # wywołanie funkcji
print(resurt)

def sort_numbers_other(*args, **kwargs): # *args określa dowolną liczbę argumentów, **kwargs tworzy słownik {'name': 'Adam'}
#    {'color': 'blue'} itd.
    print(kwargs)
    temp = list(args)
    return  sorted(temp)

resurt = sort_numbers_other(1, 4, 5, 6, 7, 2, 3, name="Adam", color="blue")  # wywołanie funkcji
print(resurt)


def sort_numbers_other(a, b, *args, c=4, **kwargs):  # kolejność najpierw zdefiniowanie argumenty na sztywno,
# później *args(nieokreślonia liczba argumentów),następnie na sztywno zdefiniowane argumenty przypisane name="Adam"
# i na końcu nieokreślona liczba argumentów przypisanych **kwargs  TO JEST KOLEJNOŚĆ UŻYCIA WSZYSTKICH RODZAJI ARGUMENTÓW


# KLASY/ Class

class Ball:
    color = "red"
    size = 3
# powyżej jest tylko definicja klasy
# musimy poniżej stworzyć obiekt/ instancję tej klasy powyżej

ball_1 = Ball()
print(ball_1.size)  # wywołujemy rodzaj atrybutu poprzez (.) i rodzaj atrybutu, w tym przypadku =3 z def.

ball_2 = Ball()
print(ball_2.size)  # wywołujemy rodzaj atrybutu poprzez (.) i rodzaj atrybutu, w tym przypadku =3 z def.

ball_2.size = 5     # przypisujemy wartość atrybutu poprzez (.size=5) i rodzaj atrybutu w tym przypadku =5
print(ball_2.size)



class Ball:
    # tworzymy funkcję w klasie
    def __init__(self, color_temp="red", size_temp=30):   # to nazywamy metodami - konstruktor (możemy określać atrybuty
        # (pewne cechy) # ale również metody (pewne działania).
        self.color = color_temp  # te atrubutu pochodzą z zewnątrz (color_temp), self.color - pochodzi z wewnątrz klasy
        self.size = size_temp    # te atrubutu pochodzą z zewnątrz (size_temp), ssize.color - pochodzi z wewnątrz klasy
    def show_attributes(self):
        print('Ball attrs: ')
        print(self.color)
        print(self.size)

ball_1 = Ball("blue", 40)
ball_1.show_attributes()  # print idzie z podanych argumentów "blue" i 40 - z drugiej def



class Operations:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def add_numbers(self):
        return self.number1 + self.number2

    def multiplay_numbers(self):
        return self.number1 * self.number2


op = Operations(3, 4)
print(op.add_numbers())
print(op.multiplay_numbers())

