import pytest
import random

from generator import generate_random_string
from classes import Mathematics, Logistics, Strings


def setup_module( module ):
	# init something
	pass


def teardown_module( module ):
	# destroy something
	pass


def test_upper():
	assert 'foo'.upper() == 'FOO'


def test_isupper():
	assert 'FOO'.isupper()


def test_sort():
	for i in range(100):
		arr = random.choices( range(100), k = 10 )
		arr_sorted = sorted( arr )
		arr.sort()

		assert arr == arr_sorted


def test_math():
	for i in range(100):
		int1 = random.randint( -10000, 10000 )
		int2 = random.randint( 1, 10000 )

		assert Mathematics.plus( int1, int2 ) == int1 + int2
		assert Mathematics.minus( int1, int2 ) == int1 - int2
		assert Mathematics.divide( int1, int2 ) == int1 / int2
		assert Mathematics.multiply( int1, int2 ) == int1 * int2


def test_divide_error():
	for i in range(100):
		int1 = random.randint( -1000, 1000 )
		int2 = 0

		with pytest.raises( ZeroDivisionError ):
			Mathematics.divide( int1, int2 )


def test_math_all():
	for i in range(100):
		int1 = random.randint( -1000, 1000 )
		int2 = random.randint( -1000, 1000 )

		assert Mathematics.all( int1, int2 ) == [ int1 + int2, int1 - int2, int1 * int2, int1 / int2 ]


def test_equally():
	for i in range(100):
		int1 = random.randint( -5, 5 )
		int2 = random.randint( -5, 5 )

		assert Logistics.equally( int1, int2 ) == ( int1 == int2 )


def test_strings_invert():
	for i in range(100):
		length = random.randint(2, 40)
		str = generate_random_string(length)

		assert Strings.invert(str) == str[::-1]
