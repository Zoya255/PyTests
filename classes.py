# ================= #
#                   #
#  Примеры классов  #
#                   #
# ================= #
#
#  ООП - Объектно-ориентированное программирование
#
#  class name:
#      def name():
#          pass
#


class Mathematics:
	@staticmethod
	def plus( a, b ):
		return a + b

	@staticmethod
	def minus( a, b ):
		return a - b

	@staticmethod
	def multiply( a, b ):
		return a * b

	@staticmethod
	def divide( a, b ):
		if b == 0:
			raise ZeroDivisionError
		else:
			return a / b

	@staticmethod
	def all( a, b ):
		answers = [0, 0, 0, 0]

		answers[0] = Mathematics.plus(a, b)
		answers[1] = Mathematics.minus(a, b)
		answers[2] = Mathematics.multiply(a, b)
		answers[3] = Mathematics.divide(a, b)

		return( answers )


class Logistics:
	@staticmethod
	def big( a, b ):
		if a > b:
			return a
		elif b > a:
			return b
		else:
			return False

	@staticmethod
	def small( a, b ):
		if a < b:
			return a
		elif b < a:
			return b
		else:
			return False

	@staticmethod
	def equally( a, b ):
		if a == b:
			return True
		else:
			return False


class Strings:
	@staticmethod
	def invert( string ):
		return string[::-1]
