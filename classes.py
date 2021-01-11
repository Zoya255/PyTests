#
#  ООП - Объектно-ориентированное программирование
#
#  class name:
#      def name():
#          pass
#


class mathematics:
	def plus( self, a, b ):
		return a + b

	def minus( self, a, b ):
		return a - b

	def multiply( self, a, b ):
		return a * b

	def divide( self, a, b ):
		return a / b

	def all( self, a, b ):
		list = [0, 0, 0, 0]

		list[0] = self.plus(a, b)
		list[1] = self.minus(a, b)
		list[2] = self.multiply(a, b)
		list[3] = self.divide(a, b)

		print( list )

		for item in list:
			print( item )


class logistics:
	def big( self, a, b ):
		if a > b:
			return a
		elif b > a:
			return b
		else:
			return False

	def small( self, a, b ):
		if a < b:
			return a
		elif b < a:
			return b
		else:
			return False

	def equally( self, a, b ):
		if a == b:
			return True
		else:
			return False


class string:
	def invert( self, string ):
		return string[::-1]
