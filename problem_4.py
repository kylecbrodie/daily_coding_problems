from random import randint

def first_missing_positive_integer(integers: [int]) -> int:
	num_integers = len(integers)
	if num_integers == 0:
		return 1

	# With this C style for loop we will place the positive integers in the
	# list at the index they should be
	#      [1, 2, 3, ...]
	#       0, 1, 2, ... (0-based index)
	#       1, 2, 3, ... (1-based index)
	# So when we traverse the list a second time we'll know which is the first
	# positive integer missing by the incorrect value at the index.
	# E.g. [1, 2, 3, -10, ...] tells us 4 is the first positive integer missing
	# because if there was a 4 in the original list it would have been placed
	# at 0-based index 3 by this loop
	i = 0
	while i < num_integers:
		integer = integers[i]
		# if integer - 1 is a valid index and the element at index integer - 1 is not equal to integer
		if 0 < integer <= num_integers and integers[integer - 1] != integer:
			# swap the element at index integer - 1 with the element at index i
			integers[i], integers[integer - 1] = integers[integer - 1], integers[i]
			# if we swap forwards re-evaluate integers[i] because it is a value
			# we haven't placed yet
			if integer > i:
				continue
		i += 1

	for i, integer in enumerate(integers, 1):
		if integer != i:
			return i

	return num_integers + 1

assert 1 == first_missing_positive_integer([])
assert 2 == first_missing_positive_integer([1])
assert 3 == first_missing_positive_integer([1, 2, 0])
assert 2 == first_missing_positive_integer([3, 4, -1, 1])
assert 5 == first_missing_positive_integer([3, 2, 4, -1, 1])
assert 6 == first_missing_positive_integer([5, 4, 3, 2, 1])
assert 1 == first_missing_positive_integer([-99, -32, 60, -59, 88, 4, -18, 8, -12, -47, \
											-6, 51, -3, 74, -12, -16, -22, 11, 3, -6, 13, \
											25, -41, 99, 57, -36, -77, 96, 88, -11, 75, 71, \
											-49, -4, -42, -34, -84, 94, -42, -62, 94, -70, \
											13, 95, 63, 97, 90, -94, 72, -100])
assert 51 == first_missing_positive_integer([i for i in range(50, 0, -1)])
assert 51 == first_missing_positive_integer([50] + [i for i in range(1, 50)])

for i in range(100):
	integers = [randint(-100, 100) for j in range(50)]
	sorted_integers = sorted(integers)
	print(sorted_integers)
	missing_pos_int = 1
	for integer in sorted_integers:
		if integer == missing_pos_int:
			missing_pos_int += 1
		if integer > missing_pos_int:
			break
	assert missing_pos_int == first_missing_positive_integer(integers)