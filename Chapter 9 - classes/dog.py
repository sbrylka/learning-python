class Dog():
	'''Próba modelowania psa'''
	
	def __init__(self, name, age):
		'''Inicjalizacja atrybutów name i age'''
		self.name = name
		self.age = age
		
	def sit(self):
		'''Symulacja siadania po otrzymaniu polecenia'''
		print(self.name.title() + " teraz siedzi.")
		
	def roll_over(self):
		'''Symulacja przewrotu na plecy po otrzymaniu polecenia'''
		print(self.name.title() + " teraz położył się na plecy!")
		
my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 5)

print("Mój pies ma na imię " + my_dog.name.title() + ".")
print("Mój pies ma " + str(my_dog.age) + " lat.")

my_dog.sit()
my_dog.roll_over()

print("Twój pies ma na imię " + your_dog.name.title() + ".")
print("Twój pies ma " + str(your_dog.age) + " lat.")

your_dog.sit()
your_dog.roll_over()
	
