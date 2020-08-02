favorite_languages = {
	'janek': 'python',
	'sara': 'c',
	'edward': 'ruby',
	'paweł': 'python',
	}
	
ankietowani = ['janek', 'michał', 'sara', 'kamila']

for ankietowany in ankietowani:
	if ankietowany not in favorite_languages.keys():
		print(ankietowany.title() + ", weź udział w ankiecie.")
	else:
		print(ankietowany.title() + ", dziękujemy za Twój udział.")
