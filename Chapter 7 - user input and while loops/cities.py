prompt = "\nPodaj nazwy miast, które chciałbyś odwiedzić:"
prompt += "\n(Gdy zakończysz podawanie miast, napisz 'koniec'.) "

while True:
	city = input(prompt)
	
	if city == 'koniec':
		break
	else:
		print("\nChciałbym odwiedzić " + city + "!")
