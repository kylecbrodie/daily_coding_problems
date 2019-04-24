class Solution:
	def firstMissingPositive(self, integers):
		"""
		:type nums: List[int]
		:rtype: int
		"""
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