users = ['admin', 'Sebastian', 'Yarek', 'Grzesiek', 'Asia']

for user in users:
	if user == 'admin':
		print("Witaj, admin! Czy chcesz przejrzeć dzisiejszy raport?")
	else:
		print("Witaj, " + user.title() + 
		"! Dziękujemy, że ponownie się zalogowałeś!")
