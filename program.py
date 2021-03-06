#============================================#
#                                            #
#  Простая программа для расчёта математики  #
#                                            #
#============================================#


if __name__ == '__main__':
	print("-----------------------------")
	print("  Простой расчёт математики  ")
	print("-----------------------------")
	print()

	print("Выберите режим:")
	print("  | 1. Расчёт площади")
	print("  | 2. Расчёт периметра")
	print("  | 3. Всё что можно")
	print()

	regime = int(input("Режим: "))
	print()

	print("Выберите фигуру:")
	print("  | 1. Квадрат")
	print("  | 2. Прямоугольник")
	print("  | 3. Прямоугольный треугольник")
	print()

	figure = int(input("Фигура: "))
	print()

	if figure == 1:
		a = int(input("Сторона квадрата: "))

		if regime == 1:
			print("Площадь квадрата:", a * a)
		elif regime == 2:
			print("Периметр квадрата:", a * 4)
		elif regime == 3:
			print("Площадь квадрата:", a * a)
			print("Периметр квадрата:", a * 4)
		else:
			print("Неизвестный режим")

	elif figure == 2:
		a = int(input("Верхняя сторона: "))
		b = int(input("Левая сторона: "))

		if regime == 1:
			print("Площадь прямоугольника:", a * b)
		elif regime == 2:
			print("Периметр прямоугольника:", (a + b) * 2)
		elif regime == 3:
			print("Площадь прямоугольника:", a * b)
			print("Периметр прямоугольника:", (a + b) * 2)
		else:
			print("Неизвестный режим")

	elif figure == 3:
		a = int(input("Верхняя сторона: "))
		b = int(input("Левая сторона: "))

		if regime == 1:
			print("Площадь прямоугольного треугольника:", (a * b) / 2)
		elif regime == 2:
			print("Периметр прямоугольного треугольника: n/a")
		elif regime == 3:
			print("Площадь прямоугольного треугольника:", (a * b) / 2)
			print("Периметр прямоугольного треугольника: n/a")
		else:
			print("Неизвестный режим")

	else:
		print("Неизвестная фигура")

	print()
	print(f"Выбранный режим был {regime}, а фигура - {figure}")
	print()
