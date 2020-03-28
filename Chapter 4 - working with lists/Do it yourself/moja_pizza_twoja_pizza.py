pizzas = ['hawajska', 'pepperoni', 'wiejska']

friends_pizzas = pizzas[:]
friends_pizzas.append('diabolo')

for pizza in pizzas:
	print("Moja ulubiona pizza to: " + pizza.title())

for pizza in friends_pizzas:
	print("Ulubiona pizza mojego przyjaciela to: " + pizza.title())

