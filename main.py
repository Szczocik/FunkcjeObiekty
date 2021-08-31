#  plik warsztatowy Funkcje Obiekty PEP

# Funkcje to nazwane i odizolowane fragmenty kodu, które opcjonalnie mogą zwracać
# wartość: funkcje definiuje się przez jej nazwę, parametry i ciało (kod właśiciwy funkcji).

# Składnia:
# def nazwa_funkcji(parametr1, parametr2, parametr3, ... ,parametrn): #dwukropek na końcu
# 	kod do wykonania linia 1 #zwróć uwagę na wcięcie
# 	kod do wykonania linia 1
#  	kod do wykonania linia 1


# Funkcje
'''
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
'''
def sort_numbers(a, b, c=1, d=3):  # w nawiasie argumenty pozycyjne
    print("c", c)
    print("d", d)
    temp = [a, b, c, d]  # lista
    return sorted(temp)  # zwraca sortowanie listy

sorted_numbers = sort_numbers(2, 3, d=1, c=5)  # nie ma znaczenia kolejność argumentów przypisanych (c,d)
print(sorted_numbers)
