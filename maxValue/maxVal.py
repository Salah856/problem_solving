# Function to find maximum value of the expression
# (A[l] - A[k] + A[j] - A[i]) where l > k > j > i
def maximizeExpression(A):

	# create 4 lookup tables and initialize them to float('-inf')
	first = [float('-inf')] * (len(A) + 1)
	second = [float('-inf')] * len(A)
	third = [float('-inf')] * (len(A) - 1)
	fourth = [float('-inf')] * (len(A) - 2)

	# first stores the maximum value of A[l]
	for i in reversed(range(len(A))):
		first[i] = max(first[i + 1], A[i])

	# second stores the maximum value of A[l] - A[k]
	for i in reversed(range(len(A) - 1)):
		second[i] = max(second[i + 1], first[i + 1] - A[i])

	# third stores the maximum value of A[l] - A[k] + A[j]
	for i in reversed(range(len(A) - 2)):
		third[i] = max(third[i + 1], second[i + 1] + A[i])

	# fourth stores the maximum value of A[l] - A[k] + A[j] - A[i]
	for i in reversed(range(len(A) - 3)):
		fourth[i] = max(fourth[i + 1], third[i + 1] - A[i])

	# maximum value would be present at fourth[0]
	return fourth[0]


if __name__ == '__main__':

	A = [3, 9, 10, 1, 30, 40]

	# list should have atleast 4 elements
	if len(A) >= 4:
		print(maximizeExpression(A))

