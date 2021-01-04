class Car:

	# базовые методы

	def __init__(self, spawn_x=0, spawn_y=0, car_color="#ffffff", car_fuel=10, car_max_fuel=10, car_fuel_consum=1):
		self.x = spawn_x
		self.y = spawn_y
		self.color = car_color
		self.fuel = car_fuel
		self.max_fuel = car_max_fuel
		self.fuel_consum = car_fuel_consum

	def __str__(self):
		return "Базовый класс для машинок"

	# методы перемещения

	def teleport(self, tp_x, tp_y):
		self.x, self.y = tp_x, tp_y

	def move(self, direction, distance):
		if direction == 1:
			self.move_up(distance)
		elif direction == 2:
			self.move_right(distance)
		elif direction == 3:
			self.move_down(distance)
		elif direction == 4:
			self.move_left(distance)

	def move_up(self, distance):
		self.y += distance
		self.fuel_consumption(distance)

	def move_right(self, distance):
		self.x += distance
		self.fuel_consumption(distance)

	def move_down(self, distance):
		self.y -= distance
		self.fuel_consumption(distance)

	def move_left(self, distance):
		self.x -= distance
		self.fuel_consumption(distance)

	# методы солярки

	def fuel_consumption(self, distance):
		self.fuel -= ( self.fuel_consum * distance )

	def set_full_fuel(self):
		self.fuel = self.max_fuel

	def get_fuel(self, percentage = False):
		if percentage:
			return ( self.fuel / self.max_fuel ) * 100
		else:
			return self.fuel

	# методы свойств

	def set_color(self, color):
		self.color = color

	def set_default(self):
		self.x = 0
		self.y = 0
		self.color = "#ffffff"
		self.fuel = 10
		self.max_fuel = 10

	# методы отображения

	def draw(self):
		pass

	def clear(self):
		pass


audi = Car(10, 10)

print( f"Создана машинка с координатами {audi.x}, {audi.y}" )
print(audi.get_fuel(True))
audi.move(1, 10)
print(audi.get_fuel(True))
print( f"Координаты {audi.x}, {audi.y}" )

print()
print()
print()

camaro = Car(20, 10)

print( f"Создана машинка с координатами {camaro.x}, {camaro.y}")
print(camaro.get_fuel(True))
camaro.move(1, 5)
print(camaro.get_fuel(True))
print( f"Координаты {camaro.x}, {camaro.y}")

print()
print()
print()
