kot = "Pixel"
pies = "kora"
rok = 2020

print(kot == 'pixel')
print(pies == 'kora')
print(kot.lower() == 'pixel')
print(pies.lower() == 'pixel')
print(rok > 2021)
print(rok <2021)
print(rok >=2021)
print(rok <= 2021)
print(rok == 2020 and pies == 'Pixel')
print(rok == 2020 and pies == 'kora')
print(rok == 2020 or pies == 'Pixel')
print(rok == 2021 or pies == 'Pixel')

lista = ['kora', 'pixel']
if 'pomidor' in lista:
	print("Jest pomidor na liście!")

if 'pixel' in lista:
	print("Jest Pixel na liście!")
	
lista = ['kora', 'pixel']
if 'pomidor' not in lista:
	print("Nie ma pomidora na liście!")

if 'pixel' not in lista:
	print("Nie ma Pixela na liście!")

