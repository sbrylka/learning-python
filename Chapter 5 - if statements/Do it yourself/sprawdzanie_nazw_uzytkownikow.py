current_users = ['admin', 'Sebastian', 'Yarek', 'Grzesiek', 'Asia']
new_users = ['Ania', 'Yarek', 'SEBASTIAN']

current_users = [current_user.lower() for current_user in current_users]

for new_user in new_users:
	if new_user.lower() in current_users:
		print("Nazwa użytkownika jest zajęta!")
	else:
		print("Nazwa użytkownika jest wolna!") 
