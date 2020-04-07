alien_0 = {'color': 'zielony', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("Zdobyłeś " + str(new_points) + " punktów!")

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print("\nObcy ma kolor " + alien_0['color'] + ".")

alien_0['color'] = 'żółty'
print("\nObcy ma teraz kolor " + alien_0['color'] + ".")

alien_0['speed'] = 'średnio'
print("\nPoczątkowa wartość x_posiition: " + str(alien_0['x_position']))

if alien_0['speed'] == 'wolno':
	x_increment = 1
elif alien_0['speed'] == 'średnio':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("Nowa wartość x_position: " + str(alien_0['x_position']))

del alien_0['points']
print(alien_0)

###

alien_0 = {'color': 'zielony', 'points': 5}
alien_1 = {'color': 'zółty', 'points': 10}
alien_2 = {'color': 'czerwony', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
	print(alien)
	
###

aliens = []
for alien_number in range(30):
	new_alien = alien_0 = {'color': 'zielony', 'points': 5, 'speed': 'wolno'}
	aliens.append(new_alien)
	
for alien in aliens[:5]:
	print(alien)
print("...")

print("Całkowita liczna obcych: " + str(len(aliens)))

for alien in aliens[0:3]:
	if alien['color'] == 'zielony':
		alien['color'] = 'żółty'
		alien['speed'] = 'średnio'
		alien['points'] = 10
	elif alien['color'] == 'żółty':
		alien['color'] = 'czerwony'
		alien['speed'] = 'szybko'
		alien['points'] = 15

for alien in aliens[:5]:
	print(alien)
print("...")

