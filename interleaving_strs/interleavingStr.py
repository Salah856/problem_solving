# Function to check if X and Y are interleaving of S or not
def interleaved(X, Y, S):

	# return true if we have reached end of all Strings
	if not X and not Y and not S:
		return True

	# return false if we have reached the end of S
	# but X or Y are not empty
	if not S:
		return False



	# if X is not empty and its first character matches with
	# first character of S, recur for remaining substring
	if X and S[0] == X[0]:
		return interleaved(X[1:], Y, S[1:])

	# if Y is not empty and its first character matches with
	# first character of S, recur for remaining substring
	if Y and S[0] == Y[0]:
		return interleaved(X, Y[1:], S[1:])

	return False


if __name__ == '__main__':

	X = "ABC"
	Y = "DEF"
	S = "ADEBFC"

	if interleaved(X, Y, S):
		print("Given String is interleaving of X and Y")
	else:
		print("Given String is a not interleaving of X and Y")

