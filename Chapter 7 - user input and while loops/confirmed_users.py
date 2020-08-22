unconfirmed_users = ['alicja', 'bartek', 'katarzyna']
confirmed_users = []

while unconfirmed_users:
	current_user = unconfirmed_users.pop()
	
	print("Weryfikacja użytkownika " + current_user.title() + " .")
	confirmed_users.append(current_user)

print("\nZweryfikowano wymieniony poniżej użytkowników:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())
