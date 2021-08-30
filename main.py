#  plik warsztatowy Funkcje Obiekty PEP

# Funkcje to nazwane i odizolowane fragmenty kodu, które opcjonalnie mogą zwracać
# wartość: funkcje definiuje się przez jej nazwę, parametry i ciało (kod właśiciwy funkcji).

# Składnia:
'''
def nazwa_funkcji(parametr1, parametr2, parametr3, ... ,parametrn): #dwukropek na końcu
	kod do wykonania linia 1 #zwróć uwagę na wcięcie
	kod do wykonania linia 1
 	kod do wykonania linia 1
'''
rows = [
  ("Styczeń", {"Saldo": 1200, "Wpłaty": 1800, "Wydatki": 1300}),
  ("Luty", {"Saldo": 1300, "Wpłaty": 1900, "Wydatki": 1200}),
]

for name, row in rows:
  print("*" * 10)
  print("Saldo miesięczne: {}".format(name))
  print("*" * 10)
  for k,v in row.items():
  	print("{}: {}".format(k, v))
print("*" * 10)