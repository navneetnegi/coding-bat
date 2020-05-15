def double_char(str):

	'''
	Given a string, return a string where for every char in the original, there are two chars.
	'''
	new_str = ''

	for i in str:

		new_str = new_str + i*2

	return new_str

def count_hi(str):

	'''
	Return the number of times that the string "hi" appears anywhere in the given string.
	'''
	count = 0

	for i in range(len(str)-1):

		count += str[i] == 'h' and str[i+1] == 'i'

	return count


def cat_dog(str):

	'''
	Return True if the string "cat" and "dog" appear the same number of times in the given string.
	'''
	return str.count('cat') == str.count('dog')


def count_code(str):

	'''
	Return the number of times that the string "code" appears anywhere in the given string, 
	except we'll accept any letter for the 'd', so "cope" and "cooe" count.
	'''
	count = 0

	for in range(len(str)-3):

		count += str[i] == "c" and str[i+1] == "o" and str[i+3] = "e"

	return count




def end_other(a, b):

	'''
	Given two strings, return True if either of the strings appears at the very end of the other string, 
	ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
	Note: s.lower() returns the lowercase version of a string.
	'''

	x = a.lower()
	y = b.lower()

	if x.endswith(y.lower()) or y.endswith(x.lower()):

		return True
	else:
		return False


def xyz_there(str):

	'''
	Return True if the given string contains an appearance of "xyz" 
	where the xyz is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
	'''
	
	if str[:3] == 'xyz':

		return True

	for i in range(len(str()-1)):

		if str[i-1] != '.' and str[i:i+3] == 'xyz':

			return True

	return False

