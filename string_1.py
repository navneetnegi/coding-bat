#This is a exercise of coding bat String-1

def hello_name(name):

	'''

	Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!"

	'''

	print("Hello " + name + "!")

	return "Hello" + name

hello_name("Bob")


def make_abba(a,b):

	'''
	Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi"

	'''

	print(a+b+b+a)

	return a+b+b+a

make_abba("Hi","Bye")


def make_tags(tag,word):

	'''
	The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> 
	which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".

	'''

	print("<"+ tag +">" + word	+ "<"+"/"+ tag + ">")

	return("<" + tag + ">"+ word + "<"+ "/" + tag + ">")

make_tags("i","Yay")


def make_out(out,word):

	"""
	Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".

	"""

	return out[:2] + word + out[2:]

make_out('<<>>', 'Yay')


def extra_end(str):

	'''
	Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

	'''
	return str[-2:]*3


def first_two(str):

	'''
	Given a string, return the string made of its first two chars, so the String "Hello" yields "He". 
	If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

	'''

	if len(str) > 2:

		print(str[:2])

		return str[:2]

	else:

		return str[::]


def first_half(str):

	'''
	Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

	'''	

	if len(str) % 2 == 0:

		return str[0:int(len(str)/2)]


	else:

		return str

first_half("WooHoo")


def without_end(str):

	'''

	Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2
	
	'''

	if len(str) >= 2:

		return str[1:-1]

	else:

		return "String length is less than 2 characters"

without_end("s")


def combo_string(a,b):

	'''

	Given 2 strings, a and b, return a string of the form short+long+short, 
	with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

	'''
	if len(a) < len(b) or len(a) == len(b) == 0:

		print(a+b+a)

		return a+b+a

	elif len(b) < len(a):

		print(b+a+b)

		return b+a+b

	else:

		print("The strings are of same length")

combo_string("Hi","Hello")


def non_start(a,b):

	'''
	Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

	'''

	if len(a) and len(b) >= 1:

		print(a[1:]+b[1:])

		return a[1:]+b[1:]

	else:

		print("One or both the string/s has no characters")

		return "One or both the string/s has no characters"

non_start("","There")


def left2(str):

	'''
	Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

	'''

	if len(str) >= 2:

		print(str[2:] + str[:2])

		return str[2:] + str[:2]

	else:

		print("The length of string is less than two characters")

		return "The length of string is less than two characters"

left2("Hello")
