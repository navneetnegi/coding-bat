def cigar_party(cigars,is_weekend):

	'''

	When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars 
	is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
	Return True if the party with the given values is successful, or False otherwise

	'''

	if is_weekend:

		return cigars >=40


	else:

		return cigars >=40 and cigars <=60

cigar_party(50,True)