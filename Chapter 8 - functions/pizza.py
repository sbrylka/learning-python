def make_pizza(size, *toppings):
		'''podsumowanie informacji o przygotowanej pizzy'''
		print("\nPrzygotowuję pizzę o wielkości " + str(size) +
		" cm, z następującymi dodatkami:")
		for topping in toppings:
			print("- " + topping)
			
make_pizza(40, "pepperoni")
make_pizza(30, "pieczarki", "zielona papryka", "podwójny ser")
