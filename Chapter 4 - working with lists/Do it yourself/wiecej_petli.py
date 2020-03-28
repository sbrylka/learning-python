my_foods = ['pizza', 'falafel', 'ciasto z marchwi']
friends_foods = my_foods [:]

my_foods.append('cannolo')
friends_foods.append('lody')

print("Moje ulubione potrawy to:")
for food in my_foods:
	print(food)

print("\nUlubione potrawy mojego przyciela to:")
for food in friends_foods:	
	print(food)
