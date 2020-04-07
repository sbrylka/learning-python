favorite_languages = {
	'janek': 'python',
	'sara': 'c',
	'edward': 'ruby',
	'paweł': 'python',
	}

print("Ulubiony język programowania Sary to " + 
	favorite_languages['sara'].title() + ".")

for name, language in favorite_languages.items():
	print("Ulubiony język programowania użytkownika " + name.title() +
		" to " + language.title() + ".")

for name in favorite_languages.keys():
	print(name.title())
	
for name in favorite_languages:
	print(name.title())

friends = ['paweł', 'sara']

for name in favorite_languages.keys():
	print(name.title())
	
	if name in friends:
		print("Witaj, " + name.title() +
			"! Widzę, że Twoim ulubionym językiem programowania jest " +
			favorite_languages[name].title() + "!")
	
if 'elżbieta' not in favorite_languages.keys():
	print("\nElżbieta, proszę, weż udział w naszej ankiecie!")
	
for name in sorted(favorite_languages.keys()):
	print(name.title() + ", dziękujemy za udział w ankiecie!")
	
print("\nW ankiecie zostały wymienione następujące języki programowania:")
for language in favorite_languages.values():
	print(language.title())
	
print("\nW ankiecie zostały wymienione następujące języki programowania:")
for language in set(favorite_languages.values()):
	print(language.title())

###

favorite_languages = {
	'janek': ['python', 'ruby'],
	'sara': ['c'],
	'edward': ['ruby', 'go'],
	'paweł': ['python', 'haskell'],
	}
	
for name, languages in favorite_languages.items(): 
	print("\nUlibione języki programowania użytkownika " + name.title()
	+ " to:")
	for language in languages:
		print("\t" + language.title())
