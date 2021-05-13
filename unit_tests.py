import unittest
import random

from classes import Mathematics


class TestUtilDate(unittest.TestCase):
	def setUp( self ):
		# init something
		pass

	def tearDown( self ):
		# destroy something
		pass

	def test_upper( self ):
		self.assertEqual( 'foo'.upper(), 'FOO' )

	def test_isupper( self ):
		self.assertTrue( 'FOO'.isupper() )

	def test_sum( self ):
		self.assertEqual( 2 + 2, 4 )

	def test_sort( self ):
		for i in range(100):
			arr = random.choices( range(100), k = 10 )
			arr_sorted = sorted( arr )
			arr.sort()

			self.assertListEqual( arr, arr_sorted )

	def test_math( self ):
		for i in range(100):
			int1 = random.randint( -1000, 1000 )
			int2 = random.randint( -1000, 1000 )

			self.assertEqual( Mathematics.plus( int1, int2 ), int1 + int2 )
			self.assertEqual( Mathematics.minus( int1, int2 ), int1 - int2 )
			self.assertEqual( Mathematics.divide( int1, int2 ), int1 / int2 )
			self.assertEqual( Mathematics.multiply( int1, int2 ), int1 * int2 )


if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase( TestUtilDate )
	unittest.TextTestRunner( verbosity = 2 ).run( suite )
