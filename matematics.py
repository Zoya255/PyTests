#==================================#
#                                  #
#  Простые математические функции  #
#                                  #
#==================================#


a = 5
b = 15


def minus( a, b ):
	print(a - b)


def plus( a, b ):
	print(a + b)


def multiply( a, b ):
	print(a * b)


def divide ( a, b ):
	print(a / b)


def test(a, b):
	if a < b:
		print( f"{b} is cool")
	elif a > b:
		print( f"{a} is cool")
	else:
		print( f"{a} and {b} is cool")


# тут будет ваша функция с оператором сравнения
def text_len(text1 = "aaa", text2 = "aab"):
	text_len1 = len(text1)
	text_len2 = len(text2)

	if text_len1 < text_len2:
		print(text2)
	elif text_len1 > text_len2:
		print(text1)
	else:
		print(text1, text2)


if __name__ == '__main__':
	minus(a, 1)
	plus(100, b)
	multiply(a,b)
	divide(20, 5)
	print()
	test(1, 1)
	print()
	text_len()
