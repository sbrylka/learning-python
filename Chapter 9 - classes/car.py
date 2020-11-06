class Car():
	"""Prosta próba zaprezentowania samochodu."""
	
	def __init__(self, make, model, year):
		"""Inicjalizacja atrybutów opisu samochodu."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0
		
	def get_descriptive_name(self):
		"""Zwrot elegancko sformatowanego opisu samochodu."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()
		
	def read_odometer(self):
		"""Wyświetla informację o przebiegu samochodu."""
		print("Ten samochód ma przejechane " + str(self.odometer_reading)
		+ " km.")
		
	def update_odometer(self, mileage):
		"""Przypisanie wartości przebiegu samochodu.
		Zmiana zostanie odrzucona przy próbie cofnięcia licznika."""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("Nie można cofnąć licznika przebiegu samochodu!")
			
	def increment_odometer(self, kilometers):
		"""Inkrementacja wartości licznika samochodu o podaną wartość"""
		self.odometer_reading += kilometers
		
class Battery():
	"""Prosta próba modelowania akumulatora samochodu elektrycznego."""
	
	def __init__(self, battery_size = 70):
		"""Inicjalizacja atrybutów akumulatora."""
		self.battery_size = battery_size
	
	def describe_battery(self):
		"""Wyświetlenie informacji o wielkości akumulatora."""
		print("Ten samochód ma akumulator o pojemności " +
		str(self.battery_size) + " kWh.")
		
	def get_range(self):
		"""Wyświetla informacje o zasięgu samochodu na podstawie
		pojemności akumulatora."""
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		
		message = "Zasięg tego samochodu wynosi około " + str(range)
		message += " km po pełnym naładowaniu akumulatora."
		print(message)

class ElectricCar(Car):
	"""Przedstawia cechy charakrerystyczne samochodu elektrycznego."""
	
	def __init__(self, make, model, year):
		"""Inicjalizacja atrybutów clasy nadrzędnej.
		Następnie inicjalizacja atrybutów charakterystyczych 
		dla samochodu elektrycznego."""
		super().__init__(make, model, year)
		self.battery = Battery()
