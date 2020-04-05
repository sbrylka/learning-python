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
