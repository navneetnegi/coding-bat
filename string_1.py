#This is a exercise of coding bat String-1


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
	