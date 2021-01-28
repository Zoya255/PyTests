# ===================== #
#                       #
#  Make Sergo for Zoya  #
#                       #
# ===================== #

a = 200
b = 100


def print_config():
	print( "a =", a )
	print( "b =", b )


def arithmetical():
	print( "a + b =", a + b )

	print( "a - b =", a - b )
	print( "b - a =", b - a )

	print( "a * b =", a * b )

	print( "a / b =", a / b )
	print( "b / a =", b / a )

	print( "a ** b =", a ** b )


def logical():
	if a > b:
		print( "a больше b" )
	elif b > a:
		print( "b больше a" )
	else:
		print( "a равно b" )


def circles():
	for i in range(1, 11):
		print(f"Зоя крутая {i} раз!")

	print()
	i = a - 10

	while i <= a:
		print(f"Зоя крутая {i} раз!")
		i += 1


def conditions(x, y, z):
	print( "x =", x )
	print( "y =", y )
	print( "z =", z )


def lists():
	easy_list = [5, 15, 25, 50, 55]

	for item in easy_list:
		print(item)

	print(easy_list[3])


def dicts():
	easy_dict = { "name": "Zoya", "age": 19, "mood": "good" }

	print( "имя:", easy_dict["name"])
	print( "возраст:", easy_dict["age"])
	print( "настроение:", easy_dict["mood"])


def strings():
	string = "привет"

	print( string )
	print( string, string )
	print( "Строка:", string )
	print( f"Строка: {string}" )
	print( string * 2 )

	print( string[0] )
	print( string[-1] )
	print( string[0:3] )
	print( string[::-1] )


def photo(board):
	print(board[::-1])


def spirit():
	# gif = input("введите свое приветствие: ")
	photo("gif")


def files():
	file_append = open("file.txt", "a")
	file_append.write("text text text\n\n")
	file_append.close()

	file_read = open("file.txt", "r")
	print(file_read.read())
	file_append.close()


if __name__ == '__main__':
	print_config()
	print()
	arithmetical()
	print()
	logical()
	print()
	circles()
	print()
	conditions(5, 25, 255)
	print()
	lists()
	print()
	dicts()
	print()
	strings()
	print()
	photo("тевирп")
	print()
	spirit()
	print()
	files()
	print()
