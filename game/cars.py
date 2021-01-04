import pygame


class Car:

	# базовые методы

	def __init__(self, car_name, spawn_x=0, spawn_y=0, car_color="#ffffff", car_fuel=10, car_max_fuel=10, car_fuel_consum=1):
		self.name = car_name
		self.x = spawn_x
		self.y = spawn_y
		self.color = car_color
		self.fuel = car_fuel
		self.max_fuel = car_max_fuel
		self.fuel_consum = car_fuel_consum

		print(f"Создана машинка:")
		print(f"  | Название: {self.name}")
		print(f"  | Координаты: {self.x}, {self.y}")
		print(f"  | Цвет: {self.color}")
		print(f"  | Топливо: {self.fuel} из {self.max_fuel}")
		print(f"  | Расход: {self.fuel_consum} литр/ход")
		print()

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
		if self.fuel_consumption(distance):
			self.y -= distance
			print(f"{self.name} | перемещено на {distance} блок вверх")
			print()

	def move_right(self, distance):
		if self.fuel_consumption(distance):
			self.x += distance
			print(f"{self.name} | перемещено на {distance} блок вправо")
			print()

	def move_down(self, distance):
		if self.fuel_consumption(distance):
			self.y += distance
			print(f"{self.name} | перемещено на {distance} блок вниз")
			print()

	def move_left(self, distance):
		if self.fuel_consumption(distance):
			self.x -= distance
			print(f"{self.name} | перемещено на {distance} блок влево")
			print()

	# методы солярки

	def fuel_consumption(self, distance):
		if self.fuel >= 1:
			self.fuel -= ( self.fuel_consum * distance )
			print(f"{self.name} | осталось {self.fuel} литров топлива")
			return True
		else:
			print(f"{self.name} | нет топлива")
			return False

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

	def get_color(self):
		return self.color

	def set_default(self):
		self.x = 0
		self.y = 0
		self.color = "#ffffff"
		self.fuel = 10
		self.max_fuel = 10

	def get_coordinates(self):
		return self.x, self.y

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y
