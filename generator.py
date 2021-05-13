import random
import string

def generate_random_string(length):
    letters_and_digits = string.ascii_letters
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string
