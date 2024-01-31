# Problem-1: How to remove characters from the first String which are present in the second String?
def remove_characters(first: str, second: str):
	# Note: Assumption: A solution that distinguishes an upper case letter and a lower case letter
	# as two distinct characters is acceptable.
	for c in second:
		first = first.replace(c, "")  # We need to assign the result back to the original string since 
	# strings are immutable in Python. So any string method returns a new string. It does not change
	# the original string.
	return first


print(remove_characters("I would like to buy a hamburger", "abc"))
