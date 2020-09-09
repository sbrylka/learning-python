def greet_users(names):
	'''Wyświetla proste powitanie każdemu użytkownikowi z listy'''
	for name in names:
		msg = "Witaj, " + name.title() + "!"
		print(msg)

usernames = ['halina', 'tymek', 'marzena']
greet_users(usernames)

