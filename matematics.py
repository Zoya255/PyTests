# ================================================= #
#                                                   #
#  Набор простейших функций для расчёта математики  #
#                                                   #
# ================================================= #


a = 5
b = 15


def minus( int1, int2 ):
	print( int1 - int2 )


def plus( int1, int2 ):
	print( int1 + int2 )


def multiply( int1, int2 ):
	print( int1 * int2 )


def divide( int1, int2 ):
	print( int1 / int2 )


def int_equal( int1, int2 ):
	if int1 < int2:
		print( f"{int2} is bigger" )
	elif int1 > int2:
		print( f"{int1} is bigger" )
	else:
		print( f"{int1} and {int2} is equal" )


# тут будет ваша функция с оператором сравнения
def text_len( str1, str2 ):
	text_len1 = len( str1 )
	text_len2 = len( str2 )

	if text_len1 < text_len2:
		print( f"{str2} is longer" )
	elif text_len1 > text_len2:
		print( f"{str1} is longer" )
	else:
		print( f"{str1} and {str2} is equal" )



if __name__ == '__main__':
	minus( a, 1 )
	plus( 100, b )
	multiply( a, b )
	divide( 20, 5 )

	print()
<<<<<<< HEAD
	test(1, 1)
	print()
	text_len()
=======

	int_equal( 1, 1 )

	print()

	text_len("string", "long string")
>>>>>>> ec4ea64c3668a1d0b91cf38954d766c2734ea558
