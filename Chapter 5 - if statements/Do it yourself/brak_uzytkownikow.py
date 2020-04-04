users = ['admin', 'Sebastian', 'Yarek', 'Grzesiek', 'Asia']

if users:
	for user in users:
		if user == 'admin':
			print("Witaj, admin! Czy chcesz przejrzeć dzisiejszy raport?")
		else:
			print("Witaj, " + user.title() + 
		"! Dziękujemy, że ponownie się zalogowałeś!")
else:
	print("Musimy znaleźć jakichś użytkowników!")
