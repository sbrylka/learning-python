players =['karol', 'martyna', 'michał', 'florian', 'ela']
print(players[0:3])
print(players[:4])
print(players[2:])
print(players[-3:])

print("Oto pierwszych trzech graczy naszej drużyny:")
for player in players[:3]:
	print(player.title())

