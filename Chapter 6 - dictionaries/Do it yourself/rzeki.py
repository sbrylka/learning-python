rzeki = {
	'nil': 'egipt',
	'wisła': 'polska',
	'sekwana': 'francja',
	}

for rzeka, kraj in rzeki.items():
	print("\n" + kraj.title() + " to kraj, przez który płynie " + rzeka.title() + ".")
	
print("\nW słowniku znajdują się rzeki takie jak:")
for rzeka in set(rzeki.keys()):
	print("\t" + rzeka.title())
	
print("\nW słowniku znajdują się kraje takie jak:")
for kraj in set(rzeki.values()):
	print("\t" + kraj.title())


