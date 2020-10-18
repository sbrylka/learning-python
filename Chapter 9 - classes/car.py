class Car():
	"""Prosta próba zaprezentowania samochodu."""
	
	def __init__(self, make, model, year):
		"""Inicjalizacja atrybutów opisu samochodu."""
		self.make = make
		self.model = model
		self.year = year
		
	def get_descriptive_name(self):
		"""Zwrot elegancko sformatowanego opisu samochodu."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
