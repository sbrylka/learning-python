requested_topping = 'pieczarki'

if requested_topping != 'anchois':
	print("Poproszę o anchois!")


requested_topping = ['pieczarki', 'cebula', 'ananas']
print('pieczarki' in requested_topping)
print('pepperoni' in requested_topping)

###

requested_topping = ['pieczarki', 'podwójny ser']

if 'pieczarki' in requested_topping:
	print("Dodaję pieczarki.")
if 'pepperoni' in requested_topping:
	print("Dodaję pepperoni.")
if 'podwójny ser' in requested_topping:
	print("Dodaję podwójny ser.")
	
print("\nTwoja pizza jest już gotowa!")

###

requested_toppings = ['pieczarki', 'boczek', 'podwójny ser']

for requested_topping in requested_toppings:
	print("Dodaję " + requested_topping + ".")
	
print("\nTwoja pizza jest już gotowa!")

###

requested_toppings = ['pieczarki', 'boczek', 'podwójny ser']

for requested_topping in requested_toppings:
	if requested_topping == 'boczek':
		print("Przepraszamy, ale obecnie nie mamy boczku.")
	else:
		print("Dodaję " + requested_topping + ".")
	
print("\nTwoja pizza jest już gotowa!")

###

requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Dodaję " + requested_topping + ".")
else:
	print("Czy jesteś chcesz pizzę bez dodatków?")
	
###

available_toppings = ['pieczarki', 'oliwki', 'boczek', 'pepperoni',
					'ananas', 'podwójny ser']

requested_toppings = ['pieczarki', 'frytki', 'podwójny ser']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Dodaję " + requested_topping + ".")
	else:
		print("Przepraszamy, ale obecnie nie mamy dodatku " + 
			requested_topping + ".")
			
print("\nTwoja pizza jest już gotowa")

