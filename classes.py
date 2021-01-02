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


mathematics().all(2, 5)


