liczby = list(range(1,10))

for liczba in liczby:
	if liczba == 1:
		print(str(liczba) + "st")
	elif liczba == 2:
		print(str(liczba) +"nd")
	elif liczba == 3:
		print(str(liczba) + "rd")
	else:
		print(str(liczba) + "th")
